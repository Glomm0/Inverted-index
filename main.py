from genericpath import isfile
import pathlib
import re
import json
import os
import mimetypes
from bs4 import BeautifulSoup
import Stemmer
import inverted_index
import encoder


index=inverted_index.InvertedIndex("D:/B_I 2371/1 lab IS/stop_words.txt")
#index.index_collection(os.getcwd()+"/collection_html")
#index.index_document("D:/B_I 2371/1 lab IS/collection_html/All's Well That Ends Well  Entire Play.htm")
#index.index_document("D:/B_I 2371/1 lab IS/collection/King_Lear.txt")
#print(index.index)
if os.path.isfile(os.getcwd()+"/collection.json"):
    file=open(os.getcwd()+"/collection.json")
    index=json.load(file,object_hook=encoder.as_index)
    file.close()
else:
    index.index_collection(os.getcwd()+"/collection_html")
    file=open(os.getcwd()+"/collection.json","w")
    print(json.dump(obj=index,cls=encoder.CustomEncoder,fp=file))
    file.close()
#print(stemmer.stemWords(["going","go"]))
index.execute_query('go')
index.execute_query('do')
index.execute_query('going')
index.execute_query('doing')
index.execute_query('brutus')
print("_")
index.execute_query("go AND do")
index.execute_query("going AND go")
index.execute_query("going AND go AND SpiderMan")
index.execute_query("going AND do AND brutus")
print("_")
index.execute_query("go OR do")
index.execute_query("going OR go")
index.execute_query("going OR go OR SpiderMan")
index.execute_query("going OR go OR brutus")