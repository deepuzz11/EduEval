from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import csv
import os
import plotly.express as px

app = Flask(__name__)

# Path to the CSV file
DATA_FILE = 'data.csv'

# Route to display the form
@app.route('/')
def index():
    ensure_csv_file()
    return render_template('index.html')

# Route to handle form submission and display analytics
@app.route('/evaluate', methods=['POST'])
def evaluate():
    faculty_name = request.form['faculty_name']
    course_code = request.form['course_code']
    course_name = request.form['course_name']
    category = request.form['category']
    academic_year = request.form['academic_year']
    value = request.form['value']
    
    ensure_csv_file()

    if not is_duplicate(faculty_name, course_code, academic_year):
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([faculty_name, course_code, course_name, category, academic_year, value])
    
    return redirect(url_for('performance'))

# Route to display performance analytics and interactive performance
@app.route('/performance')
def performance():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        return '<p>No data available for performance analysis.</p>'

    display_option = request.args.get('option', 'static')

    if display_option == 'interactive':
        fig = px.bar(df, x='Category', y='Score', title='Scores by Category')
        graph_html = fig.to_html(full_html=False)
        return render_template('interactive_performance.html', graph_html=graph_html)
    
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

# Route for feedback submission
@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_text = request.form['feedback']
    # Handle the feedback submission here (e.g., save to a file or database)
    with open('feedback.txt', 'a') as f:
        f.write(f"{feedback_text}\n")
    return redirect(url_for('index'))

# Function to ensure CSV file exists
def ensure_csv_file():
    if not os.path.isfile(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Faculty Name', 'Course Code', 'Course Name', 'Category', 'Academic Year', 'Score'])

# Function to check for duplicate entries
def is_duplicate(faculty_name, course_code, academic_year):
    df = pd.read_csv(DATA_FILE)
    return not df[(df['Faculty Name'] == faculty_name) & (df['Course Code'] == course_code) & (df['Academic Year'] == academic_year)].empty

if __name__ == '__main__':
    app.run(debug=True)
