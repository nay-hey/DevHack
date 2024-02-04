
from flask import Flask, render_template, request, redirect, flash, session,jsonify

from flask_pymongo import PyMongo
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash
from simpleeval import simple_eval
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://<username>:<password>@cluster0.your-cluster.mongodb.net/test'
#add your mongodb atlas credential

app.config['SECRET_KEY'] = 'your secret key'
#your random sekret key
mongo = PyMongo(app)







class User:
    def init(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

# Global variable to store DataFrame
df = None

@app.route('/')
def index():
    return render_template('index_chartjs.html')

@app.route('/dashboard', methods=['POST', 'GET'])  # Allow both POST and GET methods
def dashboard():
    global df  # Use the global variable
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

            return render_template('dashboard_chartjs.html', labels=labels, data=data,df=df)

    # For GET requests, check if df is None
    if df is None:
        return "Upload a CSV file first."

    # Render the template with df
    return render_template('dashboard_chartjs.html', df=df)

@app.route('/ask_question', methods=['GET', 'POST'])
def ask_question():
    global df

    if df is None:
        return jsonify({'answer': 'DataFrame is not yet uploaded. Upload a CSV file first.'})

    if request.method == 'POST':
        try:
            data = request.get_json()

            # Check if the necessary keys are present in the JSON data
            if 'question_type' not in data or 'question_column' not in data:
                return jsonify({'answer': 'Invalid form data. Missing required keys.'})

            question_type = data['question_type']
            question_column = data['question_column']

            # Placeholder answer
            answer = "Placeholder answer."

            # Implement AI/ML-based logic
            if question_type == 'sort':
                # Sort the DataFrame based on the selected column
                sorted_df = df.sort_values(by=question_column).reset_index(drop=True)
    
                # Format the sorted DataFrame into HTML
                sorted_html = sorted_df.to_html(index=False)

                # Save the sorted DataFrame for future reference
                df = sorted_df.copy()

                # Include the HTML representation of the sorted DataFrame in the answer
                answer = f"Sorted DataFrame by {question_column}:\n{sorted_html}"


            elif question_type == 'search':
                # Check if 'search_value' is present in the JSON data
                if 'search_value' not in data:
                    return jsonify({'answer': 'Invalid form data. Missing search_value for search.'})

                search_value = data['search_value']

                # Search for rows where the specified column contains the search value
                result_df = df[df[question_column] == search_value]
                answer = f"Search results for {question_column} = {search_value}: \n{result_df}"

            elif question_type == 'aggregate':
                # Check if 'aggregation_function' is present in the JSON data
                if 'aggregation_function' not in data:
                    return jsonify({'answer': 'Invalid form data. Missing aggregation_function for aggregate.'})

                aggregation_function = data['aggregation_function']

                # Perform aggregation on the specified column based on the selected function
                if aggregation_function == 'sum':
                    result = df[question_column].sum()
                elif aggregation_function == 'mean':
                    result = df[question_column].mean()
                elif aggregation_function == 'max':
                    result = df[question_column].max()
                elif aggregation_function == 'min':
                    result = df[question_column].min()
                else:
                    return jsonify({'answer': 'Invalid aggregation_function. Supported functions: sum, mean, max, min.'})

                answer = f"Aggregated {question_column} using {aggregation_function}: {result}"

            # Add more cases for other question types

            # Return the answer as JSON
            elif question_type == 'ml_classification':
                if 'target_column' not in data:
                    return jsonify({'answer': 'Invalid form data. Missing target_column for ml_classification.'})

                target_column = data['target_column']  # Access data using the correct key
                if target_column not in df.columns:
                    return jsonify({'answer': f'Target column {target_column} does not exist in the DataFrame.'})

                features = df.drop(columns=[target_column])
                target = df[target_column]

                X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

                model = RandomForestClassifier()
                model.fit(X_train, y_train)

                predictions = model.predict(X_test)

                accuracy = accuracy_score(y_test, predictions)

                # Format the answer as a table
                headers = ['Feature', 'Importance']
                rows = list(zip(features.columns, model.feature_importances_))

                answer = {'headers': headers, 'rows': rows, 'accuracy': accuracy}

            elif question_type == 'basic_analysis':
                # Perform basic data analysis (descriptive statistics)
                descriptive_stats = df.describe()
                descriptive_stats_transposed = descriptive_stats.transpose()

                # Format the answer as a dictionary
                answer = {
                'questionType': 'basic_analysis',
                'headers': list(descriptive_stats_transposed.columns),
                'rows': [list(descriptive_stats_transposed.iloc[i]) for i in range(len(descriptive_stats_transposed))]
                }

            return jsonify({'answer': answer})

        except Exception as e:
            return jsonify({'answer': f'Error: {str(e)}'})

    # If it's a GET request, you might want to handle it differently or return an error
    return render_template('ask_question.html', df=df)



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
            return redirect('/')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = mongo.db.users.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']  # Set the username in the session
            flash('Login successful.', 'success')
            # Add any additional logic you need after a successful login
            return redirect('/')  # Redirect to index page after login
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the 'username' key from the session
    flash('You have been logged out.', 'success')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
