class DocumentRelevance:
    def __init__(self,doc_id) -> None:
        self.doc_id=doc_id
        self.relevance=0
    def get_doc_id(self):
        return self.doc_id
    def get_relevance(self):
        return self.relevance
    def update_relevance(self,tf):
        self.relevance+=tf
    def __str__(self) -> str:
        return f"doc_id:{self.doc_id}, relevance:{self.relevance}"