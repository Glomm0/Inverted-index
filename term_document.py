import math
class TermDocument:
    def __init__(self,doc_id) -> None:
        self.doc_id=doc_id
        self.tf=0
        self.tf_idf=0
    def get_doc_id(self):
        return self.doc_id
    def increase_frequncy(self):
        self.tf+=1
    def compute_tfidf(self,idf):
        self.tf_idf=(1+math.log10(self.tf))*idf
    def get_tfidf(self):
        return self.tf_idf
    def __str__(self) -> str:
        return f'doc_id:{self.doc_id}, tf:{self.tf}, tf-idf:{self.tf_idf}'