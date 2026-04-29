# RAG Fundamentals Assignment

## Objective

Build a simple Retrieval Augmented Generation pipeline and compare chunking strategies.

---

## Query Used

`Which tool is used to store vectors in a RAG pipeline?`

---

## Fixed Size Chunking

### Total Chunks Created

1

### Top Retrieved Chunks

**Chunk 1:**

```text
React Query helps cache server state. Redux manages global state. LangChain helps build LLM applications. Chroma is a vector database.
```

### Final LLM Response

```text
Based on the provided context, Chroma seems to be the tool that could potentially be used to store vectors in a RAG (Retrieve, Analyze, Generate) pipeline as it is mentioned as a vector database. However, without more specific information about the RAG pipeline, this answer might not be 100% accurate.
```

---

## Overlapping Chunking

### Total Chunks Created

1

### Top Retrieved Chunks

**Chunk 1:**

```text
React Query helps cache server state.
Redux manages global state.
LangChain helps build LLM applications.
Chroma is a vector database.
```

### Final LLM Response

```text
The context provided does not mention any tool named RAG or its usage within the given tools (React Query, Redux, LangChain, Chroma). Therefore, I'm unable to determine which tool is used to store vectors in a RAG pipeline based on the provided information.
```

---

## Semantic Chunking

### Total Chunks Created

1

### Top Retrieved Chunks

**Chunk 1:**

```text
React Query helps cache server state.
Redux manages global state.
LangChain helps build LLM applications.
Chroma is a vector database.
```

### Final LLM Response

```text
Chroma is the tool that is used to store vectors in a RAG (Retrieval-Augmented Generation) pipeline, as mentioned in your context.
```

---

## Comparison Summary

| Strategy | Strength | Weakness |
|---------|----------|----------|
| Fixed Size | Simple and fast | May cut context badly |
| Overlapping | Better recall due to shared context | More storage needed |
| Semantic | Meaningful chunks | Slightly slower / depends on formatting |

---

## Insights

- Overlapping chunking often improves recall because important text is not split abruptly.
- Semantic chunking usually gives cleaner context when documents are paragraph based.
- Fixed chunking is easiest to implement but may miss relationships across boundaries.
- Best strategy depends on document type and retrieval goals.

---

## Conclusion

Chunking strategy directly impacts retrieval quality in RAG systems. Choosing the right strategy improves answer relevance and reduces hallucinations.
