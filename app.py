import json
from nltk.stem import WordNetLemmatizer
import jsonpickle as jsonpickle
from flask import Flask, render_template, send_file, request
from flask_cors import CORS
import pandas as pd
import re
import numpy as np
from rank_bm25 import BM25Okapi

from prefit_search import*
from NLPSearch import*
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sentiment_search as ss
import nltk.data
import nltk
import re
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize



app = Flask(__name__)
CORS(app)
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

nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')

userRecords = ""


@app.route('/')
def index():
    global userRecords
    if len(userRecords) == 0:
        return jsonpickle.encode({"[]"})
    print("userRecords",userRecords)
    userRecords =  ' '.join(w for w in re.split(r"\W", userRecords) if w)
    text_tokens = word_tokenize(userRecords)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    query = ' '.join(tokens_without_sw)
    print("testindex",query)
    index = prefit_rank(query,5)
    send = []
    for t in index:
        genre = ", ".join(df_.iloc[t][14].split("'")[1::2])
        release_date = "Unknown"
        if str(df_.iloc[t][1]) != "nan":
            release_date = df_.iloc[t][1]
        curr = {
            "title" : df_.iloc[t][2],
            "release_date":release_date,
            "artist" : df_.iloc[t][5],
            "genre": genre,
            "spotify_link" : df_.iloc[t][11],
            "lyric": df_.iloc[t][30]
        }
        send.append(curr)
    return jsonpickle.encode(send),200



#http://127.0.0.1:5000/bm25_lyrics?keyword=They-re-rotting-my-brain
@app.route('/bm25_lyrics')
def bm25():
    keyword = request.args.get("keyword")
    return jsonpickle.encode(bm25_rank(All_doc, keyword))

#http://127.0.0.1:5000/prefit_qsearch?keyword=They-re-rotting-my-brain
@app.route('/prefit_qsearch')
def prefit_qsearch():
    global userRecords
    keyword = request.args.get("keyword")
    query = keyword
    query = query.replace('-', ' ')
    query = query.lower()
    userRecords += " "
    userRecords += query
    index = prefit_rank(query,5)
    send = []
    for t in index:
        genre = ", ".join(df_.iloc[t][14].split("'")[1::2])
        release_date = "Unknown"
        if str(df_.iloc[t][1]) != "nan":
            release_date = df_.iloc[t][1]
        curr = {
            "title" : df_.iloc[t][2],
            "release_date":release_date,
            "artist" : df_.iloc[t][5],
            "genre": genre,
            "spotify_link" : df_.iloc[t][11],
            "lyric": df_.iloc[t][30]
        }
        send.append(curr)
    return jsonpickle.encode(send),200

@app.route('/self_cosinesim')
def self_cosinesim():
    global userRecords
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
    userRecords += " "
    userRecords += query
    query_bow = query_BOW(query)
    query_fr = query_num(query_bow,allkey)
    query_tf = query_computeTF(query_fr,query_bow)
    query_rank = self_cosine_similarity(query_tf,tfidf,query_tf)


    index = np.argsort(query_rank)[-5:]
    send = []
    for t in index:
        genre = ", ".join(df_.iloc[t][14].split("'")[1::2])
        release_date = "Unknown"
        if str(df_.iloc[t][1]) != "nan":
            release_date = df_.iloc[t][1]
        curr = {
            "title" : df_.iloc[t][2],
            "release_date":release_date,
            "artist" : df_.iloc[t][5],
            "genre": genre,
            "spotify_link" : df_.iloc[t][11],
            "lyric": df_.iloc[t][30]
        }
    return jsonpickle.encode(send), 200


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
        resp.append(t)
    return jsonpickle.encode(resp)


if __name__ == '__main__':
    app.run()
