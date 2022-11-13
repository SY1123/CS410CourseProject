import pandas as pd
import re
import math
import numpy as np
from rank_bm25 import BM25Okapi

df = pd.read_csv("originSongs.csv", encoding='unicode_escape',sep=",")
ll = df['lyrics'].to_list()
cleanedList = [x for x in ll if x != 'NaN']
cleanedList
ll[1]
len(df.columns)
# cleanedList

df_ = df[df.lyrics != 'Error: Could not find lyrics.']
df_ = df_[df_['lyrics'].notna()]
ll = df_['lyrics'].to_list()

print(type(ll))

All_doc = ll
delimi = ",.!?/&-:;@'..."
All_bagofwords = []
for i in range(0,len(All_doc)):
    re.split("["+"\\".join(delimi)+"]", All_doc[i])
    All_doc[i] = ' '.join(w for w in re.split(r"\W", All_doc[i]) if w)
    # print(All_doc[i].split())
    All_bagofwords.append(All_doc[i].split())
print(All_bagofwords[0])

MAP = []
for i in range(0,len(All_bagofwords)):

    numWords = dict.fromkeys(All_bagofwords[i],0)
    for word in All_bagofwords[i]:
        numWords[word] +=1
    # print("map",numWords)
    MAP.append(numWords)
print(MAP[0])


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
print(TF[0])


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
print(dict(list(idf.items())[36:49]))


def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

# print(idf['finished'] * TF[0])

tfidf = []
for i in range(0, len(TF)):
    tfidf.append(computeTFIDF(TF[i],idf))
print(tfidf[36:37])

def cosine_sim(a, b):
    cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cos_sim


tokenized_corpus = [doc.split(" ") for doc in All_doc]

bm25 = BM25Okapi(tokenized_corpus)
query = "I m a little unsteady A little unsteady"
tokenized_query = query.split(" ")

doc_scores = bm25.get_scores(tokenized_query)
# array([0.        , 0.93729472, 0.        ])


print(bm25.get_top_n(tokenized_query, All_doc, n=1))