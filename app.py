from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()