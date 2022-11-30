import json

# import jsonpickle as jsonpickle
from flask import Flask, render_template, send_file, request
import os
import pandas as pd
import re
import math
import numpy as np
from rank_bm25 import BM25Okapi
from NLPSearch import*
import sentiment_search as ss

app = Flask(__name__)

df = pd.read_csv("songs.csv", encoding='unicode_escape',sep=",")
ll = df['lyrics'].to_list()
cleanedList = [x for x in ll if x != 'NaN']
# cleanedList


df_ = df[df.lyrics != 'Error: Could not find lyrics.']
df_ = df_[df_['lyrics'].notna()]
ll = df_['lyrics'].to_list()

#clean data to All_doc
All_doc = ll
delimi = ",.!?/&-:;@'..."
All_bagofwords = []
for i in range(0,len(All_doc)):
    re.split("["+"\\".join(delimi)+"]", All_doc[i])
    All_doc[i] = (' '.join(w for w in re.split(r"\W", All_doc[i]) if w)).lower()
    # print(All_doc[i].split())
    All_bagofwords.append(All_doc[i].split())
    

@app.route('/bm25_index')
def bm25():
    keyword = request.args.get("keyword")
    print(keyword)
    
    return bm25_index(All_doc, keyword),200


@app.route('/self_cosinesim')
def self_cosinesim():
    keyword = request.args.get("keyword")
    MAP = fetchInMap(All_bagofwords)
    allkey = mergeKey(MAP)
    TF = []
    for i in range(0,len(All_bagofwords)):
        tf = computeTF(MAP[i],All_bagofwords[i])
        TF.append(tf)
    idf = computeIDF(MAP,allkey)
    tfidf = []
    for i in range(0, len(TF)):
        tfidf.append(computeTFIDF(TF[i],idf))
        
    query = keyword
    query = query.lower()
    query_bow = query_BOW(query)
    query_fr = query_num(query_bow,allkey)
    query_tf = query_computeTF(query_fr,query_bow)
    query_rank = cosine_similarity(query_tf,tfidf,query_tf)
    
    
    import numpy as np
    index = np.argsort(query_rank)[-5:]
    return str(index[0]) ,200


# use: 127.0.0.1：5000/sentiment_search？keyword=xxx
@app.route('/sentiment_search')
def sentiment_search():
    keyword = request.args.get("keyword")
    if len(keyword) == 0:
        return "error, input is invalid"
    res = musicCorpus.sentiment_search(keyword)
    resp = []
    for t in res:
        if t is None:
            continue
        resp.append(jsonpickle.encode(t))
    return jsonpickle.encode(resp)


if __name__ == '__main__':
    app.run()
