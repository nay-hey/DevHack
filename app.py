from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://roopikasaxena19:rWYPB8V2GM9s7zrc@cluster0.yal08d9.mongodb.net/'
mongo = PyMongo(app)

# User model
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

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

# ...

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = mongo.db.users.find_one({'username': username})

        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
        else:
            new_user = User(username, password)
            mongo.db.users.insert_one({'username': new_user.username, 'password': new_user.password})
            flash('Account created successfully. You can now log in.', 'success')
            return redirect(url_for('index'))  # Redirect to index page after registration

    return render_template('register.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = mongo.db.users.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            flash('Login successful.', 'success')
            # Add any additional logic you need after a successful login
            return redirect(url_for('index'))  # Redirect to index page after login
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)
