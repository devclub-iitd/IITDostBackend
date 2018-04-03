from flask import Flask, render_template, logging
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def index():
	online_users = mongo.db.users.find({'online': True})
	return render_template('index.html', online_users=online_users)
	# app.logger.info(app.name)

if __name__ == '__main__':
	app.run(debug=True)