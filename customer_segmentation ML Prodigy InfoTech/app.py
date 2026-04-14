from flask import Flask, render_template
from src.preprocess import load_data, select_features
from src.kmeans_model import train_kmeans
from src.visualize import plot_clusters

app = Flask(__name__)

@app.route('/')
def home():
    df = load_data('data/Mall_Customers.csv')
    X = select_features(df)

    model, y_kmeans = train_kmeans(X, k=5)

    # Generate cluster plot
    plot_clusters(X, y_kmeans, model)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)