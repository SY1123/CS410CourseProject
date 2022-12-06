import json
from nltk.stem import WordNetLemmatizer
import jsonpickle as jsonpickle
from flask import Flask, render_template, send_file, request
import pandas as pd
import re
import math
import numpy as np
from rank_bm25 import BM25Okapi
from prefit_search import*
from NLPSearch import*

import sentiment_search as ss

app = Flask(__name__)
lemmatizer = WordNetLemmatizer()
df = pd.read_csv("songs.csv", encoding='unicode_escape',sep=",")

df_ = df[df.lyrics != 'Error: Could not find lyrics.']
df_ = df_[df_['lyrics'].notna()]
ll = df_['lyrics'].to_list()

#clean data to All_doc
All_doc = ll
delimi = ",.!?/&-:;@'..."
All_bagofwords = []
for i in range(0,len(All_doc)):
    re.split("["+"\\".join(delimi)+"]", All_doc[i])
                            #lemmatize
    All_doc[i] = (' '.join(lemmatizer.lemmatize(w) for w in re.split(r"\W", All_doc[i]) if w)).lower()
    # print(All_doc[i].split())
    All_bagofwords.append(All_doc[i].split())
    
musicCorpus = ss.Music("songs_sentiment.csv")
musicCorpus.load_data()

# @app.route('/')
# def index():
#     
#     return 200



#http://127.0.0.1:5000/bm25_lyrics?keyword=They-re-rotting-my-brain
@app.route('/bm25_lyrics')
def bm25():
    keyword = request.args.get("keyword")
    return bm25_rank(All_doc, keyword),200

#http://127.0.0.1:5000/prefit_qsearch?keyword=They-re-rotting-my-brain
@app.route('/prefit_qsearch')
def prefit_qsearch():
    keyword = request.args.get("keyword")
    query = keyword
    query = query.replace('-', ' ')
    query = query.lower()
    index = prefit_rank(query,5)
    resp = []
    for t in index:
        resp.append(jsonpickle.encode(df_.iloc[t]))
    return jsonpickle.encode(resp), 200


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
    query_rank = self_cosine_similarity(query_tf,tfidf,query_tf)
    
    
    index = np.argsort(query_rank)[-5:]
    resp = []
    for t in index:
            resp.append(jsonpickle.encode(df_.iloc[t]))
    resp = list(reversed(resp))
    return jsonpickle.encode(resp), 200


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
