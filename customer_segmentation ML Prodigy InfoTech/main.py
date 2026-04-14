from src.preprocess import load_data, select_features
from src.kmeans_model import train_kmeans
from src.visualize import plot_clusters

def main():
    df = load_data('data/Mall_Customers.csv')
    X = select_features(df)

    model, y_kmeans = train_kmeans(X, k=5)

    plot_clusters(X, y_kmeans, model)

    print("Cluster plot saved in static folder!")

if __name__ == "__main__":
    main()