from typing import List, TypedDict
from app.config import TOP_K
from app.embeddings import embed_query
from app.vector_store import query_chroma, query_qdrant

class RetrievedChunk(TypedDict):
    text: str
    source: str
    chunk_index: int
    distance: float

def retrieve(query: str, top_k: int = TOP_K, target: str = "both") -> List[RetrievedChunk]:
    query_vector = embed_query(query)
    if target in ("academic", "chroma"):
        return query_chroma(query_vector, top_k=top_k)

    if target in ("docs", "qdrant"):
        return query_qdrant(query_vector, top_k=top_k)

    chroma_k = (top_k // 2) + 1  # 3 chunks
    qdrant_k = top_k - chroma_k  # 2 chunks

    chroma_hits = query_chroma(query_vector, top_k=chroma_k)
    qdrant_hits = query_qdrant(query_vector, top_k=qdrant_k)

    combined = chroma_hits + qdrant_hits
    combined.sort(key=lambda x: x["distance"])
    return combined