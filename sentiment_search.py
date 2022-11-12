import csv
import datetime
import time


class MusicDetail(object):
    def __init__(self):
        self.title = ""
        self.lyric = ""
        self.artist = ""
        self.spotify_link = ""
        self.spotify_id = ""
        # self.genre = []
        self.sentiment = ""
        self.date = datetime.date.today()


class Music(object):
    def __init__(self, documents_path):
        self.music_set = []
        self.total_num = 0
        self.document_path = documents_path

    def load_data(self):
        csv_reader = csv.reader(open("./data.csv"))
        for line in csv_reader:
            detail = MusicDetail()
            detail.title = line[2]
            detail.lyric = line[-1]
            detail.artist = line[4]
            detail.spotify_link = line[11]
            detail.spotify_id = line[12]
            # detail.genre = [line[]]
            detail.date = line[0]
            self.music_set.append(MusicDetail)
        # Update self.number_of_documents
        self.total_num = len(self.music_set)

    def sentiment_search(self, sentiment):

        pass




def main():
    document_path = './billboard_2000_2018_spotify_lyrics.csv'
    musicCorpus = Music(document_path)
    musicCorpus.load_data()
