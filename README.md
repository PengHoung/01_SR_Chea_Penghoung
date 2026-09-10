```markdown
# Dual-Storage Local RAG Application

An offline Retrieval-Augmented Generation (RAG) system built from scratch using Python, Poetry, Ollama, ChromaDB, and Qdrant. The pipeline indexes and retrieves information across two distinct knowledge bases using tailored chunking strategies and independent vector databases.

---

## 1. How to Run the App

### Prerequisites
* **Python 3.10+** and **Poetry**
* **Ollama** installed and running locally with the required models:
  ```bash
  ollama pull nomic-embed-text
  ollama pull llama3.2

```

### Setup & Installation

1. Install project dependencies:
```bash
poetry install

```


2. Ingest documents (Offline Build Step):
Processes the raw text files, generates dense embeddings, and builds the vector indices on disk:
```bash
poetry run python -m app.ingest

```


*(Note: This creates the local `chroma_db/` and `qdrant_db/` storage directories automatically.)*
3. Verify Vector Store Retrieval (Standalone Test):
Confirms both ChromaDB and Qdrant return valid chunks independently:
```bash
poetry run python scripts/demo_vector_check.py

```


4. Launch the Interactive Chat Application:
Starts the CLI interface to query the knowledge bases:
```bash
poetry run python -m app.main

```


Type your question at the prompt, or type `exit` to quit.

---

## 2. Chunking Strategies Used and Why

All chunking logic is implemented **from scratch** using Python standard library regular expressions (`re`) without third-party text-splitting frameworks.

### Sentence-Based Chunking

* **Target Knowledge Base:** `data/Academic` (Grading policy, Wi-Fi access, Library services)
* **Implementation:** Built using a regex lookbehind assertion (`r"(?<=[.!?])\s+(?=[A-Z0-9#])"`). This pattern detects terminal sentence punctuation marks followed by a space and a capitalized character, keeping punctuation attached to each statement.
* **Rationale:** Academic documents consist of precise, standalone rules, numerical thresholds (e.g., late submission penalty percentages), and distinct constraints. Splitting at sentence boundaries isolates individual policy facts, preventing the model from retrieving excessive, irrelevant surrounding text for fine-grained factual queries.

### Paragraph-Based Chunking

* **Target Knowledge Base:** `data/Doc Material for Ingest` (Company IT support and setup guides)
* **Implementation:** Built using double newline delimiters (`r"\n\s*\n"`), which treats continuous text blocks between blank lines as individual chunks.
* **Rationale:** IT support manuals are procedural and sequential (e.g., Step-by-Step email configuration or VPN setup). Splitting instructions into isolated sentences would sever prerequisites and numbered action items from their parent context. Preserving full paragraphs ensures each retrieved chunk retains its explanatory headers, list items, and instructions intact.

---

## 3. Embedding Model Used

* **Model Name:** `nomic-embed-text` (executed locally via Ollama)
* **Output Dimensions:** 768 dimensions
* **Role in Pipeline:** Converts chunked source texts and user queries into 768-dimensional dense numerical vectors. This enables semantic similarity search using cosine distance, allowing the system to match queries with relevant documents based on contextual meaning rather than exact keyword overlap.

---

## 4. Vector Databases Used

The application implements a dual-database architecture to isolate separate document domains and evaluate different storage paradigms:

### ChromaDB (Persistent Local Storage)

* **Target Collection:** `academic_sentences`
* **Stored Content:** Sentence-split Academic policy documents (`data/Academic`).
* **Role & Implementation:** Initialized via `chromadb.PersistentClient(path="chroma_db")`. ChromaDB provides lightweight, SQLite-backed vector storage with embedded nearest-neighbor querying, managing collections dynamically without requiring predefined dimension schemas upfront.

### Qdrant (Local Embedded Disk Storage)

* **Target Collection:** `doc_material_paragraphs`
* **Stored Content:** Paragraph-split IT support guides (`data/Doc Material for Ingest`).
* **Role & Implementation:** Initialized via `QdrantClient(path="qdrant_db")` running directly on disk without Docker. Qdrant enforces strict vector validation, configured explicitly at initialization with `VectorParams(size=768, distance=Distance.COSINE)` to match the 768-dimensional output of `nomic-embed-text`.

