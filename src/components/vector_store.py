import faiss
import pickle
import numpy as np
import os


class VectorStore:

    def create_index(self, embeddings):
        """
        Create a FAISS index from embeddings.
        """

        embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(
            dimension
        )

        index.add(
            embeddings
        )

        return index

    def save_index(self, index, path):
        """
        Save FAISS index to disk.
        """

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        faiss.write_index(
            index,
            path
        )

    def load_index(self, path):
        """
        Load FAISS index from disk.
        """

        return faiss.read_index(
            path
        )

    def save_chunks(self, chunks, path):
        """
        Save chunks to disk.
        """

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        with open(path, "wb") as f:
            pickle.dump(
                chunks,
                f
            )

    def load_chunks(self, path):
        """
        Load chunks from disk.
        """

        with open(path, "rb") as f:
            return pickle.load(f)