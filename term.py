import term_document
class Term:
    list=[]
    def __init__(self,doc_id) -> None:
        self.doc_id=doc_id
        self.term_frequency_in_collection=1
        self.list.append(term_document.TermDocument(doc_id=doc_id))
    def add_document(self,doc_id):
        self.term_frequency_in_collection+=1
        if self.list[-1].get_doc_id==doc_id:
            self.list[-1].increase_frequncy()
        else:
            list.append(term_document.TermDocument(doc_id=doc_id))
    def get_document_frequency(self):
        return self.term_frequency_in_collection
    def compute_tfidf(self,idf):
        for i in list:
            i.compute_tfidf(idf)
    def get_list(self):
        return list
