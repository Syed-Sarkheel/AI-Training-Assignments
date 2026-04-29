# Production Grade RAG Assignment

## Objective

Improve retrieval relevance using keyword search, embeddings, hybrid retrieval, reranking, and metadata filtering.

---

## Query Used

`best vector database for RAG`

---

## Before Improvements (TF-IDF Only)

**Rank 1** - Score: `0.434`

```text
Chroma is a vector database used in RAG systems.
```

**Rank 2** - Score: `0.105`

```text
BM25 is a keyword ranking algorithm for retrieval.
```

**Rank 3** - Score: `0.1`

```text
FAISS is used for similarity search over embeddings.
```

### LLM Response

```text
The best vector database for RAG (Retrieval-Augmented Generation) systems, given the context provided, would be Chroma, as it is specifically mentioned as a vector database used in such systems. However, it's important to note that while Chroma is a suitable option, other vector databases could potentially also be utilized in RAG systems depending on specific project requirements and preferences.
```

---

## After Improvements (Hybrid + Filter + Rerank)

**Rank 1** - Score: `0.527`

Metadata:
- section: ai
- type: database

```text
Chroma is a vector database used in RAG systems.
```

**Rank 2** - Score: `0.213`

Metadata:
- section: ai
- type: database

```text
FAISS is used for similarity search over embeddings.
```

### LLM Response

```text
The best vector database for RAG (Retrieval-Augmented Generation) systems, considering the context provided, would be Chroma. Chroma is a vector database designed specifically for this purpose. However, FAISS can also be used in conjunction with Chroma for similarity search over embeddings.
```

---

## Retrieval Comparison

| Method | Strength | Weakness |
|-------|----------|----------|
| TF-IDF | Fast keyword search | Misses semantic meaning |
| Embeddings | Understands meaning | May miss exact keywords |
| Hybrid | Balanced relevance | Slightly more complex |
| Metadata Filter | Very precise domains | Can hide useful docs |
| Reranking | Better final order | Extra compute |

---

## Insights

- Hybrid retrieval gave the best balance of keyword + semantic matching.
- Metadata filtering improved precision for database-specific queries.
- Reranking improved final ordering of relevant results.
- Retrieval may still fail if source data lacks enough content.
- Simpler methods are faster, advanced methods are more accurate.

---

## Conclusion

Production RAG systems usually combine multiple retrieval methods instead of relying on one technique. Hybrid search with reranking provides stronger real-world relevance.
