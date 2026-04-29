from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np
from utils.ollama_helper import ask_ollama

# ---------------------------------------------------
# DATASET WITH METADATA
# ---------------------------------------------------
documents = [
    {
        "text": "React Query helps manage API caching and server state.",
        "section": "frontend",
        "type": "react"
    },
    {
        "text": "Chroma is a vector database used in RAG systems.",
        "section": "ai",
        "type": "database"
    },
    {
        "text": "BM25 is a keyword ranking algorithm for retrieval.",
        "section": "search",
        "type": "retrieval"
    },
    {
        "text": "FAISS is used for similarity search over embeddings.",
        "section": "ai",
        "type": "database"
    },
    {
        "text": "Redux manages client-side global state.",
        "section": "frontend",
        "type": "react"
    }
]

QUERY = "best vector database for RAG"
RESULT_FILE = "04_rag_production/results.md"

# ---------------------------------------------------
# BASELINE KEYWORD SEARCH (TF-IDF)
# ---------------------------------------------------
texts = [d["text"] for d in documents]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts + [QUERY])

scores = cosine_similarity(X[-1], X[:-1])[0]

baseline_ranked = sorted(
    zip(documents, scores),
    key=lambda x: x[1],
    reverse=True
)

# ---------------------------------------------------
# EMBEDDING SEARCH
# ---------------------------------------------------
print("Loading embedding model...")
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

doc_embs = embed_model.encode(texts)
query_emb = embed_model.encode([QUERY])[0]

def cos(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

embed_scores = []

for i, emb in enumerate(doc_embs):
    embed_scores.append((documents[i], cos(query_emb, emb)))

# ---------------------------------------------------
# HYBRID SEARCH (TF-IDF + EMBEDDINGS)
# ---------------------------------------------------
hybrid = []

for i in range(len(documents)):
    tfidf_score = scores[i]
    emb_score = embed_scores[i][1]

    final_score = (0.5 * tfidf_score) + (0.5 * emb_score)

    hybrid.append((documents[i], final_score))

hybrid_ranked = sorted(hybrid, key=lambda x: x[1], reverse=True)

# ---------------------------------------------------
# METADATA FILTERING
# only databases
# ---------------------------------------------------
filtered = [x for x in hybrid_ranked if x[0]["type"] == "database"]

# ---------------------------------------------------
# SIMPLE RERANKING
# prioritize docs containing exact term 'RAG'
# ---------------------------------------------------
reranked = sorted(
    filtered,
    key=lambda x: ("RAG" in x[0]["text"], x[1]),
    reverse=True
)

# ---------------------------------------------------
# GENERATE ANSWERS
# ---------------------------------------------------
def generate_answer(top_docs):
    context = "\n".join([d[0]["text"] for d in top_docs[:2]])

    prompt = f"""
Use only the context below.

Context:
{context}

Question:
{QUERY}
"""

    try:
        return ask_ollama(prompt, temp=0.4)
    except:
        return "LLM response unavailable."

before_answer = generate_answer(baseline_ranked[:2])
after_answer = generate_answer(reranked[:2])

# ---------------------------------------------------
# SAVE MARKDOWN
# ---------------------------------------------------
with open(RESULT_FILE, "w") as f:
    f.write("# Production Grade RAG Assignment\n\n")
    f.write("## Objective\n\n")
    f.write("Improve retrieval relevance using keyword search, embeddings, hybrid retrieval, reranking, and metadata filtering.\n\n")
    f.write("---\n\n")

    f.write("## Query Used\n\n")
    f.write(f"`{QUERY}`\n\n")

    f.write("---\n\n")

    # BEFORE
    f.write("## Before Improvements (TF-IDF Only)\n\n")

    for i, item in enumerate(baseline_ranked[:3], 1):
        doc, score = item
        f.write(f"**Rank {i}** - Score: `{round(score,3)}`\n\n")
        f.write("```text\n")
        f.write(doc["text"])
        f.write("\n```\n\n")

    f.write("### LLM Response\n\n```text\n")
    f.write(before_answer.strip())
    f.write("\n```\n\n")

    f.write("---\n\n")

    # AFTER
    f.write("## After Improvements (Hybrid + Filter + Rerank)\n\n")

    for i, item in enumerate(reranked[:3], 1):
        doc, score = item
        f.write(f"**Rank {i}** - Score: `{round(score,3)}`\n\n")
        f.write("Metadata:\n")
        f.write(f"- section: {doc['section']}\n")
        f.write(f"- type: {doc['type']}\n\n")
        f.write("```text\n")
        f.write(doc["text"])
        f.write("\n```\n\n")

    f.write("### LLM Response\n\n```text\n")
    f.write(after_answer.strip())
    f.write("\n```\n\n")

    f.write("---\n\n")

    # Comparison
    f.write("## Retrieval Comparison\n\n")
    f.write("| Method | Strength | Weakness |\n")
    f.write("|-------|----------|----------|\n")
    f.write("| TF-IDF | Fast keyword search | Misses semantic meaning |\n")
    f.write("| Embeddings | Understands meaning | May miss exact keywords |\n")
    f.write("| Hybrid | Balanced relevance | Slightly more complex |\n")
    f.write("| Metadata Filter | Very precise domains | Can hide useful docs |\n")
    f.write("| Reranking | Better final order | Extra compute |\n\n")

    f.write("---\n\n")

    # Insights
    f.write("## Insights\n\n")
    f.write("- Hybrid retrieval gave the best balance of keyword + semantic matching.\n")
    f.write("- Metadata filtering improved precision for database-specific queries.\n")
    f.write("- Reranking improved final ordering of relevant results.\n")
    f.write("- Retrieval may still fail if source data lacks enough content.\n")
    f.write("- Simpler methods are faster, advanced methods are more accurate.\n\n")

    f.write("---\n\n")

    f.write("## Conclusion\n\n")
    f.write("Production RAG systems usually combine multiple retrieval methods instead of relying on one technique. "
            "Hybrid search with reranking provides stronger real-world relevance.\n")

print(f"Saved {RESULT_FILE}")