import plotly.graph_objects as go
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import numpy as np
import os

# encoding_file = 'final_latent_file.txt'
# label_file = 'pred_labels.txt'
path = '/Users/bryanwgranger/Documents/sandbox/cs638/scdeepcluster/output/pbmc-500-500-2000'
in_dir = os.listdir(path)


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

        tsne = TSNE(n_components=2, init='pca', learning_rate='auto')
        d_t = tsne.fit_transform(encodings)

        fig = go.Figure(
            go.Scatter(
                x=d_t[:,0],
                y=d_t[:,1],
                mode='markers',
                marker_color=labels

            )
        )
        fig.update_layout(title_text=f"SCDeepCluster-500-500-2000 - gamma = {os.path.basename(directory).split('_')[-1]}")
        fig.write_image(os.path.join(directory, 'cluster_tsne.png'))
        fig.show()