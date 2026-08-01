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


def save_analysis(dataset_id, question, report, analysis_result):
    """
    Saves a completed analysis.
    """

    doc_id = f"{dataset_id}_{collection.count()+1}"

    collection.add(
        ids=[doc_id],
        documents=[
f"""
# ❓ Soru

{question}

---

# 📊 Test

{analysis_result["test"]}

---

# 🤖 AI Raporu

{report}
"""
],
        metadatas=[
    {
        "dataset": dataset_id,
        "question": question,
        "test": analysis_result["test"]
    }
]
    )

def get_history(dataset_id):
    """
    Returns all previous analyses for the current dataset.
    """

    results = collection.get(
        where={"dataset": dataset_id},
        include=["documents", "metadatas"]
    )

    history = []

    if results["documents"] is None:
        return history

    for doc, meta in zip(results["documents"], results["metadatas"]):
        history.append(
            {
                "question": meta["question"],
                "test": meta.get("test", "Unknown"),
                "report": doc
            }
        )

    return history

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