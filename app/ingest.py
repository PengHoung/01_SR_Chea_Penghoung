import os
import re
from typing import List, Tuple

from app.config import (
    ACADEMIC_DATA_DIR,
    DOC_MATERIAL_DATA_DIR,
    PARAGRAPH_CHUNK_SIZE,
    PARAGRAPH_CHUNK_OVERLAP,
    SENTENCE_OVERLAP_COUNT,
)
from app.embeddings import embed_texts
from app.vector_store import (
    reset_chroma,
    add_to_chroma,
    reset_qdrant,
    add_to_qdrant,
)


# ----------------- SPLITTING WITH OVERLAP -----------------
def chunk_by_sentence(
    text: str, overlap_count: int = SENTENCE_OVERLAP_COUNT
) -> List[str]:
    """Splits text on sentence boundaries (.! ?) and pairs
    consecutive sentences using a sliding window to carry
    subject and pronoun context across chunks.
    """
    raw_sentences = [
        s.strip()
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9#])", text)
        if s.strip()
    ]
    if not raw_sentences:
        return []

    # With SENTENCE_OVERLAP_COUNT = 1, pairs 2 sentences sliding forward by 1
    window_size = overlap_count + 1
    step = 1

    chunks = []
    for i in range(0, len(raw_sentences), step):
        window = raw_sentences[i : i + window_size]
        chunks.append(" ".join(window))
        if i + window_size >= len(raw_sentences):
            break

    return chunks


def chunk_by_paragraph(
    text: str,
    chunk_size: int = PARAGRAPH_CHUNK_SIZE,
    chunk_overlap: int = PARAGRAPH_CHUNK_OVERLAP,
) -> List[str]:
    """Splits text by double newlines (\n\n) and merges paragraphs up to
    PARAGRAPH_CHUNK_SIZE (500 chars), carrying forward a trailing
    PARAGRAPH_CHUNK_OVERLAP (75 chars) context buffer.
    """
    raw_paragraphs = [
        p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()
    ]
    if not raw_paragraphs:
        return []

    chunks = []
    current_chunk = ""

    for para in raw_paragraphs:
        if not current_chunk:
            current_chunk = para
        elif len(current_chunk) + len(para) + 2 <= chunk_size:
            current_chunk += "\n\n" + para
        else:
            chunks.append(current_chunk)
            # Retain a trailing overlap buffer from the prior chunk
            overlap_prefix = (
                current_chunk[-chunk_overlap:] if chunk_overlap > 0 else ""
            )
            current_chunk = (overlap_prefix + "\n\n" + para).strip()

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


# ----------------- DOCUMENT LOADER -----------------
def load_txt_files(directory: str) -> List[Tuple[str, str]]:
    docs = []
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found.")
        return docs
    for fname in sorted(os.listdir(directory)):
        fpath = os.path.join(directory, fname)
        if os.path.isfile(fpath) and fname.lower().endswith(".txt"):
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    docs.append((fname, content))
    return docs


# ----------------- INGESTION -----------------
def ingest_academic_to_chroma():
    print(
        "\n[1/2] Ingesting Academic folder -> Sentence Chunking (1-Sentence Overlap) -> ChromaDB..."
    )
    reset_chroma()
    docs = load_txt_files(ACADEMIC_DATA_DIR)

    ids, texts, metadatas = [], [], []
    for fname, content in docs:
        sentences = chunk_by_sentence(content)
        for i, s in enumerate(sentences):
            ids.append(f"{fname}::sent::{i}")
            texts.append(s)
            metadatas.append({"source": fname, "chunk_index": i})

    if texts:
        embeddings = embed_texts(texts)
        add_to_chroma(ids, texts, embeddings, metadatas)
    print(f"Indexed {len(texts)} sentence chunks into ChromaDB.")


def ingest_doc_material_to_qdrant():
    print(
        "\n[2/2] Ingesting Doc Material folder -> Paragraph Chunking (500/75 chars) -> Qdrant..."
    )
    reset_qdrant()
    docs = load_txt_files(DOC_MATERIAL_DATA_DIR)

    texts, metadatas = [], []
    for fname, content in docs:
        paragraphs = chunk_by_paragraph(content)
        for i, p in enumerate(paragraphs):
            texts.append(p)
            metadatas.append({"source": fname, "chunk_index": i})

    if texts:
        embeddings = embed_texts(texts)
        ids = list(range(len(texts)))
        add_to_qdrant(ids, texts, embeddings, metadatas)
    print(f"Indexed {len(texts)} paragraph chunks into Qdrant.")


def main():
    ingest_academic_to_chroma()
    ingest_doc_material_to_qdrant()
    print("\nAll folders ingested successfully with customized chunk overlap.")


if __name__ == "__main__":
    main()