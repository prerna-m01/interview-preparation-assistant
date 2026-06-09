import numpy as np

class Retriever:

    def __init__(self, index, chunks, embedder):

        self.index = index
        self.chunks = chunks
        self.embedder = embedder

    def retrieve(self, query, top_k=3):

        query_embedding = self.embedder.generate_embeddings(
            [query]
        )

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results