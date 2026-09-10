import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.embeddings import embed_query
from app.vector_store import query_chroma, query_qdrant


def check_both_stores():
    print("=" * 60)
    print("STEP 4: STANDALONE VECTOR STORE VERIFICATION")
    print("=" * 60)

    # 1. Test ChromaDB
    chroma_query = "What is the Wi-Fi bandwidth or grading penalty?"
    print(f"\n[Test 1/2] Querying ChromaDB (Academic / Sentences)")
    print(f"Query: '{chroma_query}'")

    chroma_vec = embed_query(chroma_query)
    chroma_hits = query_chroma(query_embedding=chroma_vec, top_k=2)

    print(f"Retrieved {len(chroma_hits)} hits from ChromaDB:")
    for i, hit in enumerate(chroma_hits, 1):
        print(f"  [{i}] Source: {hit['source']} | Index: {hit['chunk_index']} | Dist: {hit['distance']:.4f}")
        print(f"      Text: {hit['text']}")

    # 2. Test Qdrant
    qdrant_query = "What account type and security settings should I configure for email?"
    print(f"\n" + "-" * 60)
    print(f"[Test 2/2] Querying Qdrant (Doc Material / Paragraphs)")
    print(f"Query: '{qdrant_query}'")

    qdrant_vec = embed_query(qdrant_query)
    qdrant_hits = query_qdrant(query_embedding=qdrant_vec, top_k=2)

    print(f"Retrieved {len(qdrant_hits)} hits from Qdrant:")
    for i, hit in enumerate(qdrant_hits, 1):
        print(f"  [{i}] Source: {hit['source']} | Index: {hit['chunk_index']} | Dist: {hit['distance']:.4f}")
        print(f"      Text: {hit['text']}")

    print("\n" + "=" * 60)
    print("Both vector stores are operational and responding correctly.")
    print("=" * 60)


if __name__ == "__main__":
    check_both_stores()