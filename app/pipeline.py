from typing import List, Tuple
from app.config import TOP_K
from app.generate import generate_answer
from app.retrieval import retrieve


def run_pipeline(query: str, top_k: int = TOP_K) -> Tuple[str, List[dict]]:
    """
    Retrieves the top-k chunks across both stores and prompts the model.
    """
    retrieved_chunks = retrieve(query, top_k=top_k, target="both")
    answer = generate_answer(query=query, chunks=retrieved_chunks)
    return answer, retrieved_chunks