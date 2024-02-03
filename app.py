# app.py

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_chartjs.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            df = pd.read_csv(uploaded_file)

            # Get user input for column numbers
            x_column = int(request.form['x_column'])
            y_column = int(request.form['y_column'])

            # Validate user input to ensure column numbers are within the range of the DataFrame
            if x_column < 0 or x_column >= len(df.columns) or y_column < 0 or y_column >= len(df.columns):
                return "Invalid column numbers. Please enter valid numbers."

            # Get column names based on user input
            x_column_name = df.columns[x_column]
            y_column_name = df.columns[y_column]

            # Extract data for Chart.js
            labels = df[x_column_name].tolist()
            data = df[y_column_name].tolist()

            return render_template('dashboard_chartjs.html', labels=labels, data=data)

if __name__ == '__main__':
    app.run(debug=True)
