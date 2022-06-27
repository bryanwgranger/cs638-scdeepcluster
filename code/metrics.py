import plotly.graph_objects as go
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import numpy as np
import os
from sklearn.metrics import silhouette_score, calinski_harabasz_score


path = '/Users/bryanwgranger/Documents/sandbox/cs638/scdeepcluster/output/pbmc-500-500-2000'
in_dir = list(os.listdir(path))

gammas = []
sil_list = []
ch_list = []

for f in sorted(in_dir):
    directory = os.path.join(path, f)
    if os.path.isdir(directory):
        print('working on:', f)
        encoding_file = os.path.join(directory, 'final_latent_file.txt')
        label_file = os.path.join(directory, 'pred_labels.txt')
        with open(encoding_file, 'r') as f:
            encodings = np.loadtxt(f, delimiter=',')

        with open(label_file, 'r') as l:
            labels = np.loadtxt(l, dtype="int")

        gammas.append(os.path.basename(directory).split("_")[-1])
        sil_list.append(silhouette_score(encodings, labels))
        ch_list.append(calinski_harabasz_score(encodings, labels))

sil_arr = np.round(np.array(sil_list), decimals=3)
ch_arr = np.array(ch_list)
ch_arr = np.round(ch_arr/np.max(ch_arr), decimals=3)

sil_fig = go.Figure()
sil_fig.add_trace(go.Bar(
    x=gammas,
    y=sil_arr,
    text=sil_arr,
))
sil_fig.update_layout(xaxis=dict(type="category", title="Gamma value"),
                      yaxis_title='Silhouette Score',
                      title_text=f"Silhouette Scores - {os.path.basename(path)}")
sil_fig.show()
sil_fig.write_image(os.path.join(path, 'sil_score.png'))

ch_fig = go.Figure()
ch_fig.add_trace(go.Bar(
    x=gammas,
    y=ch_arr,
    text=ch_arr
))
ch_fig.update_layout(xaxis=dict(type="category", title="Gamma value"),
                     yaxis_title='Calinski-Harabasz Score (normalized)',
                     title_text=f"Calinski-Harabasz Scores - {os.path.basename(path)}")
ch_fig.show()
ch_fig.write_image(os.path.join(path, 'ch_score.png'))

