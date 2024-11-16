
# EduEval: Academic Faculty Evaluation and Analytics Platform

**EduEval** is a comprehensive platform designed to streamline the evaluation of academic faculty and analyze their performance. It helps academic institutions collect evaluation data, visualize performance metrics, and gain valuable insights into faculty performance using both traditional and advanced data analysis techniques.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Features

- **Evaluation Submission:** User-friendly interface for submitting faculty evaluations.
- **Data Visualization:** Static and interactive visualizations to understand performance metrics.
- **Machine Learning Insights:** Analyze evaluation data to identify trends and top performers.
- **Feedback Collection:** Users can submit feedback for continuous improvement of the platform.

## Technologies Used

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Data Handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Plotly
- **Machine Learning:** Scikit-learn (for future enhancements)

## Installation

To set up the EduEval project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/EduEval.git
   cd EduEval
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

5. **Access the application:**
   
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Navigate to the home page to submit faculty evaluations.
2. After submitting evaluations, explore various metrics and insights through the provided links in the navigation menu.
3. Use interactive visualizations to analyze performance trends dynamically.
4. Submit feedback using the feedback form to help improve the platform.

## File Structure

```
EduEval/
│
├── data/
│   └── data.csv                # Stores evaluation data submitted by users.
│
├── static/
│   ├── script.js               # JavaScript for interactive elements.
│   └── style.css               # CSS for styling the web application.
│
├── templates/
│   ├── index.html              # Main landing page for evaluations.
│   ├── insights.html           # Insights derived from evaluation data.
│   ├── interactive_performance.html  # Interactive visualizations page.
│   ├── metrics.html            # Detailed performance metrics page.
│   └── performance.html         # Static performance overview page.
│
├── LICENSE                      # License file for project distribution terms.
│
├── ML.ipynb                    # Jupyter Notebook for machine learning analysis.
│
├── README.md                    # Documentation file for project overview and instructions.
│
├── app.py                       # Main application file running Flask server.
│
└── feedback.txt                 # File collecting user feedback for improvements.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



Thank you for your interest in EduEval! We hope this platform enhances the evaluation process in academic institutions and provides valuable insights into faculty performance.
