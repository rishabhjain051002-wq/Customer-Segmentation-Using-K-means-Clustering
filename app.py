import pickle
from flask import Flask, request, render_template
import pandas as pd
from sklearn.cluster import KMeans

app = Flask(__name__)

# Load the saved KMeans model and the DataFrame with clusters
with open('kmeans_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('df_with_clusters.pkl', 'rb') as df_file:
    df = pickle.load(df_file)

@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        age = int(request.form['age'])
        income = float(request.form['income'])

        # Prepare the input data as a DataFrame (same format as training data)
        input_data = pd.DataFrame([[age, income]], columns=['Age', 'Annual Income (k$)'])

        # Predict the cluster for the input data
        cluster = model.predict(input_data)

        # Get the cluster center (optional)
        cluster_center = model.cluster_centers_[cluster]

        return render_template('index.html', prediction_text=f"Predicted Cluster: {cluster[0]}")
    
if __name__ == "__main__":
    app.run(debug=True)
