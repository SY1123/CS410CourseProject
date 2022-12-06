import spacy
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

datarame = pd.read_csv("songs_sentiment.csv", encoding='unicode_escape',sep=",")
datarame_ = datarame[datarame.lyrics != 'Error: Could not find lyrics.']
datarame_ = datarame_[datarame_['lyrics'].notna()]
llyrics = datarame_['lyrics'].to_list()
llyrics = list(map(lambda x: x.lower(), llyrics))


nlp = spacy.load('en_core_web_sm')
unwanted_pipes = ["ner", "parser"]

# Remove punctuation and spaces
# Filter for tokens consisting of alphabetic characters
# return the lemma (which require POS tagging).
def spacy_tokenizer(doc):
  with nlp.disable_pipes(*unwanted_pipes):
    return [t.lemma_ for t in nlp(doc) if \
            not t.is_punct and \
            not t.is_space and \
            t.is_alpha]

#Vectorized for pre fit model save time in search
#TfidfVectorizer.
vectorizer = TfidfVectorizer(tokenizer=spacy_tokenizer)
features = vectorizer.fit_transform(llyrics)


def top_k(arr, k):
  kth_largest = (k + 1) * -1
  return np.argsort(arr)[:kth_largest:-1]


def prefit_rank(query, top):
  query_tfidf = vectorizer.transform([query])
  cosine_similarities = cosine_similarity(features, query_tfidf).flatten()
  top_index = top_k(cosine_similarities, top)
  return(top_index)



