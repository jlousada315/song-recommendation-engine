import streamlit as st
import sqlite3
import gensim
from operator import itemgetter
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


@st.cache(allow_output_mutation=True)
def load_my_model():
    with st.spinner('Downloading word2vec model... please hold...'):
        model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)
    return model


class WebApp:
    def __init__(self):
        self.conn = sqlite3.connect('data/songs.db')
        self.model = load_my_model()
        st.success('Done!')
        self.run()

    def find_song(self, song_name, limit=5):
        c = self.conn.cursor()
        c.execute("SELECT * FROM songs WHERE UPPER(name) LIKE '%" + song_name + "%'")
        res = sorted((x + (self.model.vocab[x[0]].count,)
                      for x in c.fetchall() if x[0] in self.model.vocab),
                     key=itemgetter(-1), reverse=True)

        return [*res][:limit]

    def suggest_songs(self, song_id):
        c = self.conn.cursor()
        similar = dict(self.model.most_similar([song_id]))
        song_ids = ', '.join(("'%s'" % x) for x in similar.keys())
        c.execute("SELECT * FROM songs WHERE id in (%s)" % song_ids)
        res = sorted((rec + (similar[rec[0]],) for rec in c.fetchall()),
                     key=itemgetter(-1),
                     reverse=True)
        return [*res]

    def visualize_embeddings(self):

        X = self.model[self.model.vocab][0:1000]

        tsne = TSNE(n_components=2)
        X_tsne = tsne.fit_transform(X)

        graph = plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
        st.write(graph)

    def run(self):
        st.set_option('deprecation.showfileUploaderEncoding', False)
        st.header("Song Recommendation Engine.")

        # Input Selection
        song = st.text_input('Name a song')
        song_id = self.find_song(song)[0][0]

        if song_id:
            st.write('Song selected:', song)
        else:
            print('song not found')
            exit()

        if st.button('Get Recomendations!'):
            for t in self.suggest_songs(song_id):
                st.write(t[1] + ' - ' + t[2])


if __name__ == '__main__':
    W = WebApp()
