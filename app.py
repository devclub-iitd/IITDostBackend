# imports
from flask import Flask, render_template, logging, redirect, url_for
# from flask_pymongo import PyMongo
from pymongo import MongoClient

# Initializing MongoDB
client = MongoClient('localhost', 27017)
db = client.iitdost

# Collections
staffs = db.staffs
students = db.students
appointments = db.appointments

# Initializing app
app = Flask(__name__)
# app.config["MONGO_DBNAME"]='iitdost'
# mongo = PyMongo(app)


# Homepage
@app.route('/')
def index():
	# online_users = mongo.db.users.find({'online': 'True'})
	online_users = staffs.find({'online': True})
	return render_template('index.html', online_users=online_users)
	# app.logger.info(app.name)

# Adding staffs
@app.route('/add_staff/<string:name>/<string:password>/')
def add_staff(username,password):
	staff = {'username':username, 'password':password, 'online':True}
	staffs.insert(staff)
	return redirect(url_for('index'))


# Remove all the data
@app.route('/refresh')
def refresh():
	# db.users.drop()
	db.staffs.drop()
	db.students.drop()
	db.appointments.drop()
	return redirect(url_for('index'))


# Starting App
if __name__ == '__main__':
	app.run(debug=True)