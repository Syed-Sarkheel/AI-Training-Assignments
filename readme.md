# LLM Assignments Repository

A beginner-friendly project containing **4 practical LLM assignments** using local models, RAG pipelines, prompt engineering, and retrieval improvements.

This repository demonstrates:

- Decoding parameter experiments
- Prompt engineering techniques
- RAG fundamentals
- Production-grade RAG improvements

---

# Project Structure

```bash
AI Tranining Assignments/
│── 01_decoding_experiment/
│   ├── main.py
│   └── results.md
│
│── 02_prompt_engineering/
│   ├── main.py
│   └── results.md
│
│── 03_rag_fundamentals/
│   ├── main.py
│   ├── sample_doc.txt
│   └── results.md
│
│── 04_rag_production/
│   ├── main.py
│   └── results.md
│
│── utils/
│   └── ollama_helper.py
│
│── requirements.txt
│── README.md
````

---

# What You Need

Install these first:

* Python 3.10+
* pip
* Git
* Ollama (for local LLM)

---

# Step 1: Clone or Open Project

```bash
cd ~/Desktop
git clone https://github.com/Syed-Sarkheel/AI-Training-Assignments.git
cd "AI Tranining Assignments"
```

If already downloaded:

```bash
cd ~/Desktop/AI Tranining Assignments
```

---

# Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 3: Install Python Packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` missing packages:

```bash
pip install requests pandas chromadb sentence-transformers scikit-learn torch
```

---

# Step 4: Install Ollama

## Ubuntu / Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Check Installation

```bash
ollama --version
```

---

# Step 5: Download a Local Model

Recommended lightweight model:

```bash
ollama pull tinyllama
```

Other options:

```bash
ollama pull phi3
ollama pull mistral // heavier model, request timed-out for lower temperatures (requires stronger machines)
```

---

# Step 6: Start Ollama

Usually Ollama runs automatically.

Test:

```bash
ollama list
```

If needed:

```bash
ollama serve
```

---

# Important: How to Run Files

Always run from project root:

```bash
cd ~/Desktop/"AI Tranining Assignments"
```

Use:

```bash
python3 -m folder_name.main
```

---

# Run Assignment 1

## Decoding Experiment

Tests different temperatures and compares outputs.

```bash
python3 -m 01_decoding_experiment.main
```

Output:

```bash
01_decoding_experiment/results.md
```

---

# Run Assignment 2

## Prompt Engineering

Includes:

* Zero-shot prompting
* Few-shot prompting
* Role prompting
* JSON structured prompting

```bash
python3 -m 02_prompt_engineering.main
```

Output:

```bash
02_prompt_engineering/results.md
```

---

# Run Assignment 3

## RAG Fundamentals

Includes:

* Fixed chunking
* Overlapping chunking
* Semantic chunking
* Vector DB retrieval
* LLM answers

```bash
python3 -m 03_rag_fundamentals.main
```

Output:

```bash
03_rag_fundamentals/results.md
```

---

# Run Assignment 4

## Production Grade RAG

Includes:

* TF-IDF retrieval
* Embedding search
* Hybrid retrieval
* Metadata filtering
* Reranking

```bash
python3 -m 04_rag_production.main
```

Output:

```bash
04_rag_production/results.md
```

---

# Run All Assignments

```bash
python3 -m 01_decoding_experiment.main
python3 -m 02_prompt_engineering.main
python3 -m 03_rag_fundamentals.main
python3 -m 04_rag_production.main
```

---

# Common Errors & Fixes

---

## ModuleNotFoundError

Run from root folder:

```bash
cd ~/Desktop/"AI Tranining Assignments"
```

Then run with:

```bash
python3 -m folder.main
```

---

## Ollama Timeout

Use lighter model:

```bash
ollama pull tinyllama
```

---

## Port 11434 Already In Use

Means Ollama already running.

Just run scripts directly.

---

## Slow Performance

Use:

* tinyllama
* Close other apps
* Ensure enough RAM

---

# Technologies Used

* Python
* Ollama
* Sentence Transformers
* ChromaDB
* Scikit-learn
* TF-IDF
* Markdown Reporting

---

# Learning Outcomes

After completing these assignments you will understand:

* How decoding parameters affect outputs
* Prompt engineering techniques
* How RAG pipelines work
* Chunking strategies
* Hybrid search systems
* Retrieval optimization techniques

---
