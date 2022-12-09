# CourseProject

## 💻 Overview

Since spotify doesn’t support lyrics based songs searching, one of our website platform focuses is to help users search songs by inputting lyrics.  A common situation we often encounter is hearing a song from somewhere and thinking it sounds good, but only remembering a few lines of lyrics. However, mainstream listening platforms do not have specific adaptations for searching songs based on lyrics, so we often encounter cases where we cannot search for the song. Therefore, this is one of the motivations of our project. And the other
feature of our project is that user can search songs based on their mood, which is achieved by sentiment analysis.
Our project is a web search platform with front-end based on React frame and back-end based on Flask. The main functionality of our search platform has three parts:

1. Given a lyrics query [any length], quick-return the top matched songs and return detail information about the song based on [cosine_similarity]

2. After user searches on the platform, the recommendation page will list out similar songs based on the search history

3. Given a keyword [stands for a mood] query, return the top 6 songs that match the sentiment expressed in the query.


## 🔧 Work Covers

- Data cleaning
- Bagofwords mapping
- TF-IDF
- Sklearn metrics pairwise
- Vectorization(pre-fit model)
- Ranker Function:
- Cosine_similarity
- Knn NearestNeighbors fit on matrix


## 💡Implementation Detail

We use the web development framework React and TypeScript for front-end development. On the home page, uers can be directed to three main pages by clicking corresponding menu item. The three main pages are recommendation page, lyrics search page and mood search page. This is achieved by using <Outlet> in React. An <Outlet> is used in the home route (parent route) to render its child route elements (Recommendation, lyrics search, and mood search component), which allows showing nested UI. The default homepage is as follows:

<div align="center">
<img src=./image/page1.jpeg width=60%/>

Figure 1 Homepage
</div>




On the recommendation page, the recommended songs will be automatically loaded on this page. On two search pages, when a user type in the target text in the search box and click the search button, the front-end will send a GET request and use the response to update the song list which stores the search results as one of the corresponding component’s state variables. Then the results will be presented under the search box. These three pages with search results are as follows.

<div align="center">
<img src=./image/page2.jpeg width=60% />

Figure 2 Recommendation page
</div>

<div align="center">
<img src=./image/page3.jpeg width=60% />

Figure 3 Lyrics search page
</div>


<div align="center">
<img src=./image/page4.jpeg width=60% />

Figure 4 Mood search page
</div>

For backend, we have functionalities such as Data Cleaning, Pre-processing, lyrics based search algorithms and sentiment based search algorithms

- Data Cleaning:
We first used pandas to read csv file into a dataframe. Then remove some rows containing ‘nan’, remove non-related characters, and remove some stopwords in the dataframe. 

- Pre-processing: 
  - On Spotify dataset: First map in lyrics of cleaned data into bag of words, then use this data structure as a base to calculate Term Frequency、IDF、TF-IDF
  - For pre-fit search: First load the nlp unwanted pipes, then tokenize the data, after that build the Vectorization of tf-idf. At last, fit the model by vectorizer fit transformation
  - Sentiment Analysis: After cleaning data in dataframe, we use sentiment.vader package from nltk to analyze every lyric and get a score for each lyric. Then, we tag each song to “positive”, ”positive+”, ”negative+”,  and “negative”. 
  - Recommendation System(KNN):
                One of our recommendation systems is based on the k-nearest neighbors algorithm. This algorithm uses labeled data to make predictions on new, unlabeled data. In our case, we use previously searched lyrics as input to predict which lyrics users may be interested in. 
  - Recommendation System(cosine similarity):
                app.py will store the lemmatized, stop-words-removed query history for the user. After user have searched some songs, a recommendation page will automatically generates the top ranked songs based on the cosine similarity between dataset and query history
  - Recommendation Default Score:
                To calculate which song is more popular, I use a formula to calculate it by weeks and ranks. This can be used to recommend songs by default.
		
- Lyrics based search algorithms
  - cosine similarity algorithm generates the top ranked songs based on the query metrics and dataset metrics. Output all the detailed information about the song.

- sentiment based search algorithms
  - First we get users’ input
  - Then we calculate the compound based on the input by using SentimentIntensityAnalyzer from nltk.sentiment.vader. Compound is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive)




### API Detail

####  Recommend songs based on user query history

*URL* : `/` 

*Method* : `GET`

*Request* : ` `

*Response* : 

| num | filed        | type   | desc                                                               |
|-----|--------------|--------|--------------------------------------------------------------------|
| 1   | title        | String | title of the song                                                  |
| 2   | lyrics       | String |                                                                    |
| 3   | genre        | String | “contemporary country, country, country road, traditional country" |
| 4   | album        | Object |                                                                    |
| 5   | release_date | String |                                                                    |
| 6   | artist       | String |                                                                    | 
| 7   | spotify_link | String |                                                                    |
| 8   | spotify_id   | String |                                                                    |
| 9   | sentiment    | String |                                                                    |
| 10  | compound     | float  |                                                                    |


#### Lyrics Based Search

*URL* : `/self_cosinesim` and `/prefit_qsearch` 

*Method* : `GET`

*Request* : 

| num | filed      | type   | desc        |
|-----|------------|--------|-------------|
| 1   | keyword    | String | input       |

*Response* : 

| num | filed        | type   | desc                                                               |
|-----|--------------|--------|--------------------------------------------------------------------|
| 1   | title        | String | title of the song                                                  |
| 2   | lyrics       | String |                                                                    |
| 3   | genre        | String | “contemporary country, country, country road, traditional country" |
| 4   | album        | Object |                                                                    |
| 5   | release_date | String |                                                                    |
| 6   | artist       | String |                                                                    | 
| 7   | spotify_link | String |                                                                    |
| 8   | spotify_id   | String |                                                                    |
| 9   | sentiment    | String |                                                                    |
| 10  | compound     | float  |                                                                    |


#### Sentiment Search

*URL* : `/sentiment_search`

*Method* : `GET`

*Request* : 

| num | filed      | type   | desc        |
|-----|------------|--------|-------------|
| 1   | keyword    | String | input       |

*Response* : 

| num | filed        | type   | desc                                                               |
|-----|--------------|--------|--------------------------------------------------------------------|
| 1   | title        | String | title of the song                                                  |
| 2   | lyrics       | String |                                                                    |
| 3   | genre        | String | “contemporary country, country, country road, traditional country" |
| 4   | album        | Object |                                                                    |
| 5   | release_date | String |                                                                    |
| 6   | artist       | String |                                                                    | 
| 7   | spotify_link | String |                                                                    |
| 8   | spotify_id   | String |                                                                    |
| 9   | sentiment    | String |                                                                    |
| 10  | compound     | float  |                                                                    |

Demo:
```json
[
    {
        "py/object":"sentiment_search.MusicDetail",
        "title":"If You Can Do Anything Else",
        "lyric":"xxx",
        "artist":"george strait",
        "spotify_link":"",
        "spotify_id":"",
        "genre":"[u'contemporary country', u'country', u'country road', u'traditional country']",
        "album":"",
        "sentiment":"positive",
        "compound":0.5719,
        "release_date":"2008/11/1"
    }
]

```

## 📦 Usage

This project is initialized with [NPM](https://www.npmjs.com/) and Python Flask. 

First, clone the source code from GitHub
```shell
git clone https://github.com/SY1123/CS410CourseProject
```

If you don't have node.js and npm, then install it from the website(https://nodejs.org/en/):

Then, to install all dependencies for the front end, run:

```shell
cd  front410
npm install
```

To start the front end , run:

```shell
npm run dev
```

Next, install python dependencies for back end:

```shell
cd ..
pip install numpy
pip install re
pip install jsonpickle
pip install nltk
pip intall pandas
pip install -u flask-cors
pip install flask
pip install scikit-surprise
pip install rank_bm25
python -m spacy download en_core_web_sm
```

To start backend server, run: 
This could be slow because it is pre-fitting the model on a pretty large dataset

```shell
flask run
```



The project does not support static build. To create an optimized production build, run:

```shell
npm run build
```

Then run the following command to start the production server:

```shell
next
```



## Contributors

|     Name      |           UIN           |   
|:-------------:|:-----------------------:|
|   Ying Sun    | yingsun3 (Team Captain) | 
|   Chang Li    |        changli8         |
| Yuteng Zhuang |        yutengz2         | 
|  Qinhan Xia   |        qinhanx2         |

 