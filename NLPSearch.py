import pandas as pd
import re
import math
import numpy as np
from rank_bm25 import BM25Okapi

df = pd.read_csv("songs_sentiment.csv", encoding='unicode_escape', sep=",")
ll = df['lyrics'].to_list()
cleanedList = [x for x in ll if x != 'NaN']
cleanedList
ll[1]
len(df.columns)
# cleanedList

df_ = df[df.lyrics != 'Error: Could not find lyrics.']
df_ = df_[df_['lyrics'].notna()]
ll = df_['lyrics'].to_list()

# print(type(ll))
#clean data to All_doc
All_doc = ll
delimi = ",.!?/&-:;@'..."
All_bagofwords = []
for i in range(0,len(All_doc)):
    re.split("["+"\\".join(delimi)+"]", All_doc[i])
    All_doc[i] = (' '.join(w for w in re.split(r"\W", All_doc[i]) if w)).lower()
    # print(All_doc[i].split())
    All_bagofwords.append(All_doc[i].split())
# print(All_bagofwords[0])


#Map word freq in each doc
MAP = []
for i in range(0,len(All_bagofwords)):

    numWords = dict.fromkeys(All_bagofwords[i],0)
    for word in All_bagofwords[i]:
        numWords[word] +=1
    # print("map",numWords)
    MAP.append(numWords)
# print(MAP[0])

allkey = set().union(*MAP)
allkey


#TF
def computeTF(wordDict, bagOfwords):
    tfDict = {}
    bagOfwordsL = len(bagOfwords)
    # print("type check:", (wordDict))
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfwordsL)
    return tfDict

TF = []
for i in range(0,len(All_bagofwords)):
    tf = computeTF(MAP[i],All_bagofwords[i])
    TF.append(tf)
    # print(tf)
# print(TF[0])



#IDF Inverse Data Frequency
def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(set().union(*MAP), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict
idf = computeIDF(MAP)
print(dict(list(idf.items())[0:20]))


def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

# print(idf['finished'] * TF[0])

tfidf = []
for i in range(0, len(TF)):
    tfidf.append(computeTFIDF(TF[i],idf))
# print(tfidf[0])
# len(tfidf[0])


#Start here is query proecessing
def query_BOW(input):
    delimi = ",.!?/&-:;@'..."
    re.split("["+"\\".join(delimi)+"]", input)
    input = ' '.join(w for w in re.split(r"\W", input) if w)
    return(input.split())

def query_num(input):
    result = dict.fromkeys(allkey, 0)
    for word in input:
        result[word] += 1
    return(result)

def query_computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

def query_computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

query = "They're rotting my brain"
query = query.lower()
query_bow = query_BOW(query)
query_fr = query_num(query_bow)
query_tf = query_computeTF(query_fr,query_bow)
len(query_tf)


import math
def cosine_similarity(query, datas):
    result = []
    for data in datas:
        numerator  = 0
        denom_q = 0
        denom_d = 0
        for key in query:
            denom_q += pow(query[key],2)
            numerator += data.get(key, 0)*query_tf[key]
        for key in data:
            denom_d += pow(data[key],2)
        result.append(numerator / (math.sqrt(denom_q) * math.sqrt(denom_d) ))
    return(result)
query_rank = cosine_similarity(query_tf,tfidf)

#this will give the index of top five rank selection for the query
#same index can be used to get other data from ll variable
import numpy as np
np.argsort(query_rank)[-5:]




def bm25_index(All_doc, query):
    
    #second choice use the bm25
    tokenized_corpus = [doc.split(" ") for doc in All_doc]

    bm25 = BM25Okapi(tokenized_corpus)
    # query = "I m a little unsteady A little unsteady"
    tokenized_query = query.split(" ")

    doc_scores = bm25.get_scores(tokenized_query)
    # array([0.        , 0.93729472, 0.        ])

    #this will directly give the lyrics
    return(bm25.get_top_n(tokenized_query, All_doc, n=1))