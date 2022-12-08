from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fuzzywuzzy import process

#clean data
df = pd.read_csv("songs.csv", encoding='unicode_escape',sep=",")
df_ = df[df.lyrics != 'Error: Could not find lyrics.']
df_ = df_[df_['lyrics'].notna()]

#set song matrix based on rank
test_df = df_.iloc[:, [2,9]]
test_df['index'] = range(1, len(df_.index)+1)
test_df['rank'] = 1 / test_df['rank'] 
movie_users=test_df.pivot(index='index', columns='title',values='rank').fillna(0)
matrix_songs=csr_matrix(movie_users.values)

#fit KNN
knn= NearestNeighbors(metric='minkowski', algorithm='brute', n_neighbors=10)
knn.fit(matrix_songs)


def KNNrecommender(movie_name, n_recommendations ):
    knn.fit(matrix_songs)
    idx=process.extractOne(movie_name, df['title'])[2]
    # print('Movie Selected:-',df['title'][idx], 'Index: ',idx)
    # print('Searching for recommendations.....')
    distances, indices=knn.kneighbors(matrix_songs[idx], n_neighbors=n_recommendations)
    [indices] = indices
    titlelist = []
    for i in indices:
        titlelist.append(df['title'][i])
    titlelist.remove(titlelist[0])
    return titlelist
