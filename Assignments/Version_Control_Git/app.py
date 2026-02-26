from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.test
collection = db['test']

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime('%A')
    return render_template('index.html', current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return form_data

if __name__ == '__main__':
    app.run(debug=True)