from flask import Flask, render_template, logging, redirect, url_for
# from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.iitdost

staffs = db.staffs
students = db.students
appointments = db.appointments

app = Flask(__name__)
# app.config["MONGO_DBNAME"]='iitdost'
# mongo = PyMongo(app)

@app.route('/')
def index():
	# online_users = mongo.db.users.find({'online': 'True'})
	online_users = staffs.find({'online': True})
	return render_template('index.html', online_users=online_users)
	# app.logger.info(app.name)

@app.route('/add/<string:name>/<string:password>/')
def add_user(username,password):
	staff = {'username':username, 'password':password, 'online':True}
	staffs.insert(staff)
	return redirect(url_for('index'))

@app.route('/refresh')
def refresh():
	# db.users.drop()
	db.staffs.drop()
	db.students.drop()
	db.appointments.drop()
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)