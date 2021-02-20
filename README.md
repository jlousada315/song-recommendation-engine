# song-recommendation-engine
This repo contains the framework for a Song Recommendation Engine based on Spotify playlists using Word2Vec. This end-to-end project starts by scrapping data from [Spotify's API](https://developer.spotify.com/documentation/web-api/), collecting over 200k playlists and 8.411.437 songs, creating a sqlite database to store them. After that, an off-the-shelf model [Word2Vec](https://radimrehurek.com/gensim/models/word2vec.html) is trained so that songs that appear on the same context (i.e. same playlists) will have similar vector representations, much like words in sentences. Finally, a web application is deployed using [Streamlit](https://www.streamlit.io), where the recommendation engine can be tested.

## 1. Collect Data

## 2. Create sqlite DataBase

## 3. Train Word2Vec

## 4. Find Similar Songs

## 5. Deploy Web Applications
