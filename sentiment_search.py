import csv
import datetime

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk.data
import heapq

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('wordnet')


class MusicDetail(object):
    def __init__(self):
        self.title = ""
        self.lyric = ""
        self.artist = ""
        self.spotify_link = ""
        self.spotify_id = ""
        self.genre = []
        self.release_date = ""
        self.sentiment = ""
        self.compound = 0.0


class Music(object):
    def __init__(self, documents_path):
        self.music_set = []
        self.total_num = 0
        self.document_path = documents_path

    def load_data(self):
        csv_reader = csv.reader(open(self.document_path, encoding='utf-8'))
        next(csv_reader)
        for line in csv_reader:
            detail = MusicDetail()
            detail.title = line[3]
            detail.lyric = line[31]
            detail.artist = line[5]
            detail.spotify_link = line[12]
            detail.spotify_id = line[13]
            detail.genre = line[16]
            #detail.album =
            detail.release_date = line[1]
            detail.sentiment = line[36]
            # print(line[-2])
            detail.compound = float(line[35])
            self.music_set.append(detail)
            # print(detail)
        # Update self.number_of_documents
        self.total_num = len(self.music_set)

    def sentiment_search(self, keyword):
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(keyword)
        compound = scores["compound"]
        q = [(abs(compound - x.compound), i) for i, x in enumerate(self.music_set)]
        heapq.heapify(q)
        res = []
        for t in range(6):
            res.append(self.music_set[heapq.heappop(q)[1]])
            # print(self.music_set[heapq.heappop(q)[1]].title)
        return res

# if __name__ == '__main__':
#     document_path = 'songs_sentiment.csv'
#
#     musicCorpus = Music(document_path)
#     musicCorpus.load_data()
#     musicCorpus.sentiment_search("happy")
