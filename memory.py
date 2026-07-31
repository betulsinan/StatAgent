import chromadb
import hashlib

# Persistent local database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="analysis_memory"
)


def get_dataset_id(df):
    """
    Creates a unique ID for the uploaded dataset.
    """
    csv_text = df.to_csv(index=False)
    return hashlib.md5(csv_text.encode()).hexdigest()


def save_analysis(dataset_id, question, answer):
    """
    Saves a completed analysis.
    """

    doc_id = f"{dataset_id}_{collection.count()+1}"

    collection.add(
        ids=[doc_id],
        documents=[
f"""
Soru:
{question}

Cevap:
{answer}
"""
],
        metadatas=[
            {
                "dataset": dataset_id,
                "question": question
            }
        ]
    )


def retrieve_memory(dataset_id, question, n_results=3):
    """
    Retrieves previous analyses from the SAME dataset.
    """
    print("=" * 80)
    print("DATABASE CONTENT")
    print(collection.get())
    print("=" * 80)
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    if (
        results["documents"]
        and len(results["documents"][0]) > 0
    ):
        return "\n\n".join(results["documents"][0])

    return ""

if __name__ == "__main__":
    print(collection.count())
    print(collection.get())