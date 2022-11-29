from genericpath import isfile
import pathlib
import re
import json
import os
import mimetypes
from bs4 import BeautifulSoup
import Stemmer
stemmer=Stemmer.Stemmer("english")
class InvertedIndex:
    def __init__(self,stop_words=[]):
        self.documents=[]
        self.index={}
        self.stop_words=stop_words
        if self.stop_words!=[]:
            with open(stop_words)as f:
                self.stop_words=stemmer.stemWords(f.read().split())
        #print(self.stop_words)
    def index_document(self,path):
        doc_number=len(self.documents)-1
        if mimetypes.guess_type(path)[0]=='text/plain':
            with open(path) as doc:
                document=doc.read().split()    
        elif  mimetypes.guess_type(path)[0]=='text/html':
            with open(path) as doc:
                
                soup=BeautifulSoup(doc).body
                document=soup.stripped_strings
        for string in document:
            for term in re.split("\W+",string) :
                word=stemmer.stemWord((term.rstrip(",.:!-?;[]").lstrip("\'[]").lower()))
                if word in self.index.keys():
                    if doc_number > self.index[word][-1]:
                        self.index[word].append(doc_number)
                elif word not in self.stop_words:
                    self.index[word]=[doc_number]              
        print(f"{doc_number}".center(4),str(path).center(90),str(len(self.index.keys())).center(5))
        #print(self.index)
    def index_collection(self,folder):
        direct=pathlib.Path(folder).glob("*.*")
        for i in direct:
            print(str(i))
            if str(i)not in self.documents:
                self.documents.append(str(i))
                self.index_document(str(i))
    def get_intersection(self,list1,list2):
        result=[]
        it1=iter(list1)
        it2=iter(list2)
        try:
            a=it1.__next__()
            b=it2.__next__()
            while True:
                if  a<b:
                    a=it1.__next__()
                elif a>b:
                    b=it2.__next__()
                else:
                    result.append(a)
                    a=it1.__next__()
                    b=it2.__next__()
                    
        except StopIteration:
            return(result)
    def get_union(self,list1,list2):
        result=[]
        it1=iter(list1)
        it2=iter(list2)
        try:
            cur_list=0
            a=next(it1,None)
            b=next(it2,None)
            if a is None:
                return list2
            elif b is None:
                return list1
            while True:
                
                if  a<b:
                    cur_list=1
                    result.append(a)
                    a=next(it1,None)
                elif a>b:
                    cur_list=2
                    result.append(b)
                    b=next(it2,None)
                else:
                    result.append(a)
                    a=next(it1,None)
                    b=next(it2,None)
                if a is None and b is None:
                    
                    raise StopIteration
                elif a is None:
                        cur_list=1
                        result.append(b)
                        raise StopIteration
                elif b is None:
                        cur_list=2
                        result.append(a)
                        raise StopIteration   
        except StopIteration:
            if cur_list==2:
                try:
                    while True:
                        a=it1.__next__()
                        
                        result.append(a)
                except StopIteration:
                    
                    return(result) 
            if cur_list==1:
                try:
                    while True:
                        a=it2.__next__()
                        result.append(a)
                except StopIteration:
                    
                    return(result) 
            return result           
    def execute_query(self,query):
        strings=[]
        try:
            temp=stemmer.stemWords(query.split(" AND "))
            for i in temp:
                    if i not in self.stop_words:
                        strings.append(i)
            #print(strings)
            if len(strings)>1:
                for num,i in enumerate(strings):
                    strings[num]=i.lower().lstrip().rstrip()
                try:
                    result=self.index[strings[len(strings)-1]]
                except KeyError:
                    result=[]
                while len(strings)>0:    
                        try:
                            temp=self.index[strings[len(strings)-1]]
                        except KeyError:
                            temp=[]
                        result=self.get_intersection(temp,result)
                        strings.pop()
            elif len(query.split(" OR "))>1:
                temp=stemmer.stemWords(query.split(" OR "))
                for i in temp:
                    if i not in self.stop_words:
                        strings.append(i)
                
                for num,i in enumerate(strings):
                    strings[num]=i.lower().lstrip().rstrip()
                try:
                    result=self.index[strings[len(strings)-1]]
                except KeyError:
                    result=[]
                while len(strings)>0:    
                        try:
                            temp=self.index[strings[len(strings)-1]]
                        except KeyError:
                            temp=[]
                        result=self.get_union(temp,result)
                        strings.pop()
            else:
                result=self.index[stemmer.stemWord(query.lower())]
        except KeyError:
        
            result=[]
        print(result)