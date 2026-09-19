class embedding_manager:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
        
    def get_embedding(self, text):
        # Call the embedding model to get the embedding for the given text
        return self.embedding_model.embed(text)