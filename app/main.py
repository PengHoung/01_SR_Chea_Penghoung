import utils.transport
import utils.session
from app.pipeline import run_pipeline

def main():
    print("=" * 60)
    print(" Local RAG Assistant Ready! (Type 'exit', 'quit', or 'q' to quit)")
    print("=" * 60)

    while True:
        try:
            query = input("Ask a question: ").strip()

            if not query:
                continue

            if query.lower() in ("exit", "quit", "q"):
                print("\nGoodbye!")
                break

            print("\nSearching documents and generating response...")
            answer, retrieved_chunks = run_pipeline(query)

            # Display Grounded Answer
            print("\n" + "=" * 25 + " Answer " + "=" * 25)
            print(answer)

            # Display Retrieved Passages & File Citations
            print("\n" + "-" * 20 + " Retrieved Context Sources " + "-" * 20)
            if not retrieved_chunks:
                print("(No chunks retrieved)")
            else:
                for idx, chunk in enumerate(retrieved_chunks, 1):
                    # Clean up multiple newlines so the output stays readable
                    snippet = chunk.get("text", "").strip().replace("\n", " ")

                    print(
                        f"[{idx}] File: {chunk['source']} | "
                        f"Chunk: {chunk['chunk_index']} | "
                        f"Distance: {chunk['distance']:.4f}"
                    )
                    print(f"    Text: \"{snippet}\"\n")
            print("=" * 58 + "\n")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()