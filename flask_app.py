from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from src.DataDashboard import DataDashboard 
import pandas as pd
import plotly.express as px
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    try:
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)

        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)

        if uploaded_file and allowed_file(uploaded_file.filename):
            df = pd.read_csv(uploaded_file)

            # Basic data analysis (you can replace this with more advanced AI analysis)
            descriptive_stats = df.describe()

            # Create a simple scatter plot using Plotly
            scatter_chart = px.scatter(df, x=df.columns[0], y=df.columns[1], title='Sample Dashboard')

            data = {
                'messages': [{'category': 'info', 'message': 'This is an information message.'}],
                'table': descriptive_stats.to_html(classes='table table-striped table-hover'),
                'chart': scatter_chart.to_html(),
                'filename': uploaded_file.filename
            }

            return jsonify(data)

        else:
            flash('Invalid file type. Please upload a CSV file.', 'error')
            return redirect(request.url)

    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(request.url)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}

if __name__ == '__main__':
    app.run(debug=True)
