# EduEval: Academic Faculty Evaluation and Analytics Platform

**EduEval** is a comprehensive platform designed to streamline the process of evaluating academic faculty and analyzing their performance. It aims to help academic institutions collect evaluation data, visualize performance metrics, and gain valuable insights into faculty performance. This platform leverages both traditional and advanced data analysis techniques to provide actionable recommendations.

## Project Overview

**EduEval** is built to serve the following key purposes:

- **Facilitate Faculty Evaluations:** Provide a user-friendly interface for submitting faculty evaluations, including details such as faculty name, course code, course name, evaluation category, academic year, and score.

- **Visualize Performance Metrics:** Generate and display performance visualizations to help understand faculty performance trends and patterns. Users can view both static and interactive graphs.

- **Analyze and Gain Insights:** Utilize machine learning algorithms to analyze the evaluation data and generate insights. This includes identifying top-performing faculty members and courses, and understanding trends over different academic years.

## Key Features

1. **Evaluation Submission:**
   - Users can input faculty evaluation data through a web form.
   - Data includes essential details like faculty name, course code, course name, category of evaluation, academic year, and score.

2. **Data Visualization:**
   - **Static Visualizations:** Created using Matplotlib, these include bar charts that display average scores by category.
   - **Interactive Visualizations:** Developed using Plotly, these charts offer interactive elements allowing users to explore the data dynamically.

3. **Machine Learning Insights:**
   - Analyze evaluation data to identify patterns and trends.
   - Provide insights into top-performing faculty members and courses.
   - Predict future performance trends based on historical data.

4. **Feedback Collection:**
   - Users can submit feedback about the platform or its features.
   - Feedback is stored in a text file for review and potential improvement of the system.

## Implementation Details

1. **Data Management:**
   - The application uses a CSV file (`data.csv`) to store evaluation data. This file is updated with new entries as they are submitted through the web form.
   - The CSV file is initialized with the necessary headers if it does not already exist.

2. **Web Application:**
   - **Backend:** Developed using Flask, a lightweight web framework in Python. The backend handles form submissions, data processing, and rendering of analytics.
   - **Frontend:** HTML templates are styled using Bootstrap, ensuring a responsive and visually appealing user interface.

3. **Performance Analytics:**
   - **Static Performance Graph:** A bar chart showing average scores by category, created using Matplotlib and displayed as a PNG image.
   - **Interactive Performance Graph:** A dynamic chart generated using Plotly, embedded in the webpage for interactive data exploration.

4. **Machine Learning Analysis:**
   - Basic machine learning techniques are applied to analyze trends and provide recommendations based on evaluation data.
   - Future enhancements may include more sophisticated models and algorithms.

5. **Feedback Handling:**
   - Feedback submitted by users is saved in a `feedback.txt` file. This allows for continuous improvement based on user input.

## Technologies Used

- **Backend**: Python
- **Frontend**: HTML, CSS, JavaScript
- **Data Handling**: Python libraries for data analysis and manipulation
- **Visualization**: JavaScript libraries for creating interactive charts and graphs

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
