from flask import Flask, render_template, request
import pandas as pd
import io
import base64
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import plotly.express as px

app = Flask(__name__)
DATA_FILE = 'data/data.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/performance')
def performance():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        return '<p>No data available for performance analysis.</p>'

    display_option = request.args.get('option', 'static')

    if display_option == 'interactive':
        # Interactive chart for average scores by category
        fig = px.bar(df, x='Category', y='Score', title='Scores by Category')
        graph_html = fig.to_html(full_html=False)
        
        # Interactive chart for clusters
        df_encoded = df.copy()
        le = LabelEncoder()
        df_encoded['Category'] = le.fit_transform(df['Category'])
        df_encoded['Academic Year'] = le.fit_transform(df['Academic Year'])
        X = df_encoded[['Score', 'Category', 'Academic Year']]
        kmeans = KMeans(n_clusters=3, random_state=0)
        df['Cluster'] = kmeans.fit_predict(X)
        fig_clusters = px.scatter(df, x='Score', y='Category', color='Cluster', title='Clusters of Faculty Evaluations')
        clusters_html = fig_clusters.to_html(full_html=False)
        
        # Add regression metrics to the interactive dashboard
        X = df[['Score']]
        y = df['Score']  # Dummy regression target for demonstration
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        reg = LinearRegression().fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        metrics_html = f"<h3>Regression Model Metrics</h3><p>Mean Squared Error: {mse:.2f}</p>"
        
        return render_template('interactive_performance.html', graph_html=graph_html, clusters_html=clusters_html, metrics_html=metrics_html)

    # Static performance visualization
    fig, ax = plt.subplots()
    df.groupby('Category')['Score'].mean().plot(kind='bar', ax=ax)
    ax.set_title('Average Scores by Category')
    ax.set_xlabel('Category')
    ax.set_ylabel('Average Score')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()

    return render_template('performance.html', img_base64=img_base64, display_option='static')

@app.route('/insights')
def insights():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        return '<p>No data available for insights.</p>'

    avg_scores_by_category = df.groupby('Category')['Score'].mean()
    top_category = avg_scores_by_category.idxmax()

    recommendations = f"<h3>Performance Insights</h3><p>The category with the highest average score is {top_category}. Consider focusing on enhancing the teaching quality in this category.</p>"

    return render_template('insights.html', recommendations=recommendations)


@app.route('/feedback', methods=['POST'])
def handle_feedback():
    feedback = request.form.get('feedback')
    if feedback:
        with open('feedback.txt', 'a') as f:
            f.write(feedback + '\n')
    return '<p>Thank you for your feedback!</p>'

if __name__ == '__main__':
    app.run(debug=True)