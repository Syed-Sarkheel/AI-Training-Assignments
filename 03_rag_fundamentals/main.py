from sentence_transformers import SentenceTransformer
import chromadb
import textwrap
import os
from utils.ollama_helper import ask_ollama

# -------------------------------------------------
# CONFIG
# -------------------------------------------------
MODEL_NAME = "all-MiniLM-L6-v2"
RESULT_FILE = "03_rag_fundamentals/results.md"
DOC_FILE = "03_rag_fundamentals/sample_doc.txt"

QUERY = "Which tool is used to store vectors in a RAG pipeline?"

TOP_K = 2

# -------------------------------------------------
# SAMPLE DOCUMENT (auto create if missing)
# -------------------------------------------------
if not os.path.exists(DOC_FILE):
    sample_text = """
React Query helps manage cached server state in frontend applications.

Redux is commonly used for managing global client state.

LangChain is a framework used for building LLM-powered applications.

Chroma is a vector database often used in Retrieval Augmented Generation systems.

FAISS is another vector search library for similarity search.

Chunking is the process of splitting documents into smaller searchable parts.

Overlapping chunking improves recall by preserving context between chunks.

Semantic chunking splits text based on meaning or paragraph boundaries.
"""
    with open(DOC_FILE, "w") as f:
        f.write(sample_text.strip())

# -------------------------------------------------
# READ DOCUMENT
# -------------------------------------------------
with open(DOC_FILE, "r") as f:
    document = f.read()

# -------------------------------------------------
# CHUNKING METHODS
# -------------------------------------------------
def fixed_chunk(text, size=220):
    return textwrap.wrap(text, width=size)

def overlap_chunk(text, size=220, overlap=60):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i+size])
        i += (size - overlap)
    return chunks

def semantic_chunk(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]

# -------------------------------------------------
# EMBEDDINGS
# -------------------------------------------------
print("Loading embedding model...")
embed_model = SentenceTransformer(MODEL_NAME)

# -------------------------------------------------
# RAG RUNNER
# -------------------------------------------------
def run_strategy(name, chunks):
    client = chromadb.Client()
    collection = client.create_collection(name=name)

    for i, chunk in enumerate(chunks):
        emb = embed_model.encode(chunk).tolist()
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[emb]
        )

    query_emb = embed_model.encode(QUERY).tolist()

    result = collection.query(
        query_embeddings=[query_emb],
        n_results=TOP_K
    )

    docs = result["documents"][0]

    context = "\n".join(docs)

    prompt = f"""
Use only the context below to answer.

Context:
{context}

Question:
{QUERY}
"""

    try:
        answer = ask_ollama(prompt, temp=0.4)
    except Exception:
        answer = "LLM response unavailable (timeout/local model issue)."

    return docs, answer

# -------------------------------------------------
# BUILD CHUNKS
# -------------------------------------------------
print("Preparing chunking strategies...")

strategies = {
    "Fixed Size Chunking": fixed_chunk(document),
    "Overlapping Chunking": overlap_chunk(document),
    "Semantic Chunking": semantic_chunk(document),
}

# -------------------------------------------------
# RUN ALL
# -------------------------------------------------
results = {}

for name, chunks in strategies.items():
    print(f"Running {name}...")
    retrieved, answer = run_strategy(
        name.lower().replace(" ", "_"),
        chunks
    )
    results[name] = {
        "chunks": chunks,
        "retrieved": retrieved,
        "answer": answer
    }

# -------------------------------------------------
# WRITE MARKDOWN
# -------------------------------------------------
with open(RESULT_FILE, "w") as f:
    f.write("# RAG Fundamentals Assignment\n\n")
    f.write("## Objective\n\n")
    f.write("Build a simple Retrieval Augmented Generation pipeline and compare chunking strategies.\n\n")
    f.write("---\n\n")

    f.write("## Query Used\n\n")
    f.write(f"`{QUERY}`\n\n")

    f.write("---\n\n")

    for name, data in results.items():
        f.write(f"## {name}\n\n")

        f.write("### Total Chunks Created\n\n")
        f.write(f"{len(data['chunks'])}\n\n")

        f.write("### Top Retrieved Chunks\n\n")

        for idx, chunk in enumerate(data["retrieved"], 1):
            f.write(f"**Chunk {idx}:**\n\n")
            f.write("```text\n")
            f.write(chunk.strip())
            f.write("\n```\n\n")

        f.write("### Final LLM Response\n\n")
        f.write("```text\n")
        f.write(data["answer"].strip())
        f.write("\n```\n\n")

        f.write("---\n\n")

    # Comparison
    f.write("## Comparison Summary\n\n")
    f.write("| Strategy | Strength | Weakness |\n")
    f.write("|---------|----------|----------|\n")
    f.write("| Fixed Size | Simple and fast | May cut context badly |\n")
    f.write("| Overlapping | Better recall due to shared context | More storage needed |\n")
    f.write("| Semantic | Meaningful chunks | Slightly slower / depends on formatting |\n\n")

    f.write("---\n\n")

    f.write("## Insights\n\n")
    f.write("- Overlapping chunking often improves recall because important text is not split abruptly.\n")
    f.write("- Semantic chunking usually gives cleaner context when documents are paragraph based.\n")
    f.write("- Fixed chunking is easiest to implement but may miss relationships across boundaries.\n")
    f.write("- Best strategy depends on document type and retrieval goals.\n\n")

    f.write("---\n\n")

    f.write("## Conclusion\n\n")
    f.write("Chunking strategy directly impacts retrieval quality in RAG systems. "
            "Choosing the right strategy improves answer relevance and reduces hallucinations.\n")

print(f"Saved {RESULT_FILE}")