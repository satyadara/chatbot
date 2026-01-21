# backend/memory.py

class VectorMemory:
    def __init__(self):
        # later this will connect to Pinecone
        self.memory = []

    def store(self, text, metadata=None):
        self.memory.append({
            "text": text,
            "metadata": metadata
        })

    def retrieve(self, query):
        # placeholder: return all memory for now
        return self.memory

