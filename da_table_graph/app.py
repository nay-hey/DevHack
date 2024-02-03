# app.py

from flask import Flask, render_template, request
import pandas as pd
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
            x_column_name = int(df.columns[x_column])
            y_column_name = int(df.columns[y_column])

            # Create a simple bar chart using Plotly based on user input
            fig = go.Figure(data=[go.Bar(x=df[x_column_name], y=df[y_column_name])])

            # Add titles and legend to the layout
            fig.update_layout(
                title_text='Sample Dashboard',
                xaxis_title=x_column_name,
                yaxis_title=y_column_name,
                showlegend=True
            )

            # Basic data analysis (you can replace this with more advanced AI analysis)
            descriptive_stats = df.describe()

            return render_template('dashboard.html', table=descriptive_stats.to_html(), chart=fig.to_html())

if __name__ == '__main__':
    app.run(debug=True)
