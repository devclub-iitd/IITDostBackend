from flask import Flask, render_template, logging, redirect, url_for
# from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.iitdost
users = db.users

app = Flask(__name__)
# app.config["MONGO_DBNAME"]='iitdost'
# mongo = PyMongo(app)

@app.route('/')
def index():
	# online_users = mongo.db.users.find({'online': 'True'})
	online_users = users.find({'online': True})
	return render_template('index.html', online_users=online_users)
	# app.logger.info(app.name)

@app.route('/add/<string:username>/<string:password>/')
def add_user(username,password):
	user = {'username':username, 'password':password, 'online':True}
	users.insert(user)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)