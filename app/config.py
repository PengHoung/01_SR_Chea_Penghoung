# --- Models ---
EMBED_MODEL = "nomic-embed-text"
GEN_MODEL = "llama3.2"
EMBEDDING_DIM = 768

# Paragraph chunking settings
PARAGRAPH_CHUNK_SIZE = 500
PARAGRAPH_CHUNK_OVERLAP = 75

# For sentence splitting
SENTENCE_OVERLAP_COUNT = 1

# --- ChromaDB (Academic: Sentence Chunking) ---
CHROMA_DIR = "chroma_db"
CHROMA_COLLECTION = "academic_sentences"
ACADEMIC_DATA_DIR = "data/Academic"

# --- Qdrant (Doc Material: Paragraph Chunking) ---
QDRANT_DIR = "qdrant_db"
QDRANT_COLLECTION = "doc_material_paragraphs"
DOC_MATERIAL_DATA_DIR = "data/Doc Material for Ingest"


#Retrieval
TOP_K = 5

#Generation
SYSTEM_PROMPT = (
    "You are a helpful assistant that answers questions using ONLY the "
    "context provided below. If the answer is not contained in the context, "
    'say "I don\'t have enough information in the documents to answer that." '
    "Do not use outside knowledge. Cite the source file name(s) you used."
)