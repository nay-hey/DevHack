# DevHack
DASHBOARD GENERATOR  
The project will involve the development of a web-based dashboard generator that allows users to upload datasets and easily create visually appealing dashboards. The dashboard will support features such as customizable charts, graphs, and tables. Additionally, the website will integrate AI/ML algorithms to automatically analyze the uploaded data, identify patterns, and provide answers to specific queries posed by the user.
## Features

- **Data Upload**: Easily upload datasets in various formats to the platform.
- **Data Visualization**: Generate interactive visualizations such as charts, graphs, and plots to better understand the data.
- **Dashboard Creation**: Create personalized dashboards to monitor key metrics and trends.
- **User-friendly Interface**: Intuitive design for easy navigation and usage.

________________________________________________________________________________________________________________________________________________________

## Instructions to run the website 

First download all the necessary languages in which the program is written in 

- Python
- Node.js

Download all the necessary packages in Python, to do so run the following command in the terminal
```
pip install Flask flask-pymongo pandas Werkzeug simpleeval scikit-learn
```
Download **app.py** from **css-code-full** branch 

Then download the following files from css-code-full to a folder named templates

- index.html
- dashboard.html
- dashboard_chartjs.html
- index_chartjs_html
- ask_question.html
- login.html
- pandalogo.png
- register.html

Download **pandalogo.png** from **css-code-full** branch

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
