from genericpath import isfile
import pathlib
import re
import json
import os
import mimetypes
from bs4 import BeautifulSoup
import Stemmer
import inverted_index
class CustomEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,inverted_index.InvertedIndex):
            return {"documents":obj.documents,"index":obj.index,"stop_words":obj.stop_words}
        return json.JSONEncoder.default(self,obj)
def as_index(dct):
    a=inverted_index.InvertedIndex()
    if "documents" in dct and "index" in dct and "stop_words" in dct:
        a.documents=dct["documents"]
        a.index=dct["index"]
        a.stop_words=dct["stop_words"]
        return a
    return dct