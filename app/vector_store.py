import os
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from app.config import (
    CHROMA_DIR,
    CHROMA_COLLECTION,
    QDRANT_DIR,
    QDRANT_COLLECTION,
    EMBEDDING_DIM,
)

# ----------------- CHROMA (Academic) -----------------
_chroma_settings = Settings(anonymized_telemetry=False)

def get_chroma_collection():
    client = chromadb.PersistentClient(path=CHROMA_DIR, settings=_chroma_settings)
    return client.get_or_create_collection(name=CHROMA_COLLECTION)

def reset_chroma():
    client = chromadb.PersistentClient(path=CHROMA_DIR, settings=_chroma_settings)
    try:
        client.delete_collection(name=CHROMA_COLLECTION)
    except Exception:
        pass
    return client.get_or_create_collection(name=CHROMA_COLLECTION)

def add_to_chroma(ids: List[str], documents: List[str], embeddings: List[List[float]], metadatas: List[Dict[str, Any]]):
    col = get_chroma_collection()
    col.add(ids=ids, documents=documents, embeddings=embeddings, metadatas=metadatas)

def query_chroma(query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
    col = get_chroma_collection()
    res = col.query(query_embeddings=[query_embedding], n_results=top_k, include=["documents", "metadatas", "distances"])
    chunks = []
    if res["documents"] and res["documents"][0]:
        for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
            chunks.append({"text": doc, "source": meta.get("source", "unknown"), "chunk_index": meta.get("chunk_index", -1), "distance": dist})
    return chunks

# ----------------- QDRANT (Doc Material) -----------------
def get_qdrant_client() -> QdrantClient:
    os.makedirs(QDRANT_DIR, exist_ok=True)
    return QdrantClient(path=QDRANT_DIR)

def reset_qdrant():
    client = get_qdrant_client()
    try:
        client.delete_collection(collection_name=QDRANT_COLLECTION)
    except Exception:
        pass
    client.create_collection(
        collection_name=QDRANT_COLLECTION,
        vectors_config=VectorParams(size=EMBEDDING_DIM, distance=Distance.COSINE),
    )
    return client

def add_to_qdrant(ids: List[int], documents: List[str], embeddings: List[List[float]], metadatas: List[Dict[str, Any]]):
    client = get_qdrant_client()
    points = [
        PointStruct(
            id=idx,
            vector=emb,
            payload={"text": doc, "source": meta.get("source", "unknown"), "chunk_index": meta.get("chunk_index", -1)},
        )
        for idx, doc, emb, meta in zip(ids, documents, embeddings, metadatas)
    ]
    client.upsert(collection_name=QDRANT_COLLECTION, points=points)

def query_qdrant(query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
    client = get_qdrant_client()
    search_results = client.query_points(
        collection_name=QDRANT_COLLECTION,
        query=query_embedding,
        limit=top_k,
    ).points

    chunks = []
    for hit in search_results:
        payload = hit.payload or {}
        chunks.append({
            "text": payload.get("text", ""),
            "source": payload.get("source", "unknown"),
            "chunk_index": payload.get("chunk_index", -1),
            "distance": 1.0 - (hit.score if hit.score is not None else 0.0),
        })
    return chunks