import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def plot_clusters(X, y_kmeans, model):
    os.makedirs('outputs', exist_ok=True)
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    labels = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']
    plt.figure(figsize=(9, 6))
    for i in range(5):
        plt.scatter(X.values[y_kmeans == i, 0], X.values[y_kmeans == i, 1], s=80, c=colors[i], label=labels[i])
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=200, c='yellow', marker='*', label='Centroids')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('outputs/cluster_plot.png')
    plt.savefig('static/cluster_plot.png')
    plt.close()
