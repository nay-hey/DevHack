# DevHack
### **DASHBOARD GENERATOR**  
The project will involve the development of a web-based dashboard generator that allows users to upload datasets and easily create visually appealing dashboards. The dashboard will support features such as customizable charts, graphs, and tables. Additionally, the website will integrate AI/ML algorithms to automatically analyze the uploaded data, identify patterns, and provide answers to specific queries posed by the user.
__________________________________________________________________________________________________________________________________________________________
### Features

- **Data Upload**: Easily upload datasets in various formats to the platform.
- **Data Visualization**: Generate interactive visualizations such as charts, graphs, and plots to better understand the data.
- **Dashboard Creation**: Create personalized dashboards to monitor key metrics and trends.
- **User-friendly Interface**: Intuitive design for easy navigation and usage.

Link to the demo video: https://youtu.be/2DXncNR16wc?feature=shared
________________________________________________________________________________________________________________________________________________________

### Instructions to run the website 

First download all the necessary languages in which the program is written in 

- Python
- Node.js

Download all the necessary packages in Python, to do so run the following command in the terminal
```
pip install Flask flask-pymongo pandas Werkzeug simpleeval scikit-learn
```
Download **app.py** from **main** branch 

Then download the following files from **main** branch to a folder named templates

- index.html
- dashboard.html
- dashboard_chartjs.html
- index_chartjs_html
- ask_question.html
- login.html
- register.html

Download **pandalogo.png** from **main** branch

## MongoDB Connection Setup

#### Step 1: Create MongoDB Atlas Account

1. Sign up on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

#### Step 2: Build a Cluster

1. Create a new cluster in MongoDB Atlas.

#### Step 3: Configure Database Access

1. In the "Database Access" section, set up a database user.

#### Step 4: Configure Network Access

1. In the "Network Access" section, whitelist your IP address.

#### Step 5: Get Connection String

1. In the cluster dashboard, click "Connect."
2. Choose "Connect Your Application" to get the connection string.

#### Step 6: Use Connection String

1. Copy the connection string, which looks like: mongodb+srv://<username>:<password>@cluster0.your-cluster.mongodb.net/test  
Replace <username> and <password> with the credentials you created.

Now you have your MongoDB connection URL. Ensure you handle this URL securely, and consider using environment variables to store sensitive information like database credentials. Never share your MongoDB connection URL in public repositories or forums.

Now put this in the code as follows: **app.config['MONGO_URI'] = 'your_mongo_uri_here'**
   
Initiate the following command in the terminal to get the JSON package
```
npm init
```
To run the website, run this command 
```
python app.py
```
Then run the following URL on the browser
```
http://127.0.0.1:5000
```

