from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    """
    Convert list of strings into embeddings
    """
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings


if __name__ == "__main__":
    sample = ["Endee is a vector database", "Python is great"]
    vectors = embed_texts(sample)
    print("Embedding shape:", vectors.shape)
