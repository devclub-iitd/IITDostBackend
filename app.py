# imports
from flask import Flask, render_template, logging, redirect, url_for, request
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

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


# Class Staff
class StaffForm(Form):
	name = StringField('Name',[validators.length(min=1, max=50)])
	dept = StringField('Department',[validators.length(min=1, max=50)])
	typef = StringField('Staff Category',[validators.length(min=1, max=50)])
	room = StringField('Room',[validators.length(min=1, max=50)])
	imgurl = StringField('imgurl',[validators.length(min=1, max=100)])

# Add Staff using form
@app.route('/add_staff/form', methods = ['GET', 'POST'])
def add_staff_form():
	form = StaffForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		dept = form.dept.data
		typef = form.typef.data
		room = form.room.data
		umgurl = form.imgurl.data
		
		staff = {'name':name, 'dept':dept, 'type':typef, 'room':room, 'online':True, 'image':request.args.get('imgurl')}
		staffs.insert(staff)
		return redirect(url_for('index'))
	return render_template('add_staff_form.html', form=form)		

# Homepage
@app.route('/')
def index():
	# online_users = mongo.db.users.find({'online': 'True'})
	online_users = staffs.find({'online': True})
	return render_template('index.html', online_users=online_users)
	# app.logger.info(app.name)

# Adding staffs
@app.route('/add_staff/<string:name>/<string:dept>/<string:typef>/<string:room>')
def add_staff(name,dept,typef,room):
	staff = {'name':name, 'dept':dept, 'type':typef, 'room':room, 'online':True, 'image':request.args.get('imgurl')}
	staffs.insert(staff)
	return redirect(url_for('index'))


# All Staffs
@app.route('/staff')
def staff():
	staff_ = staffs.find({})
	return dumps(staff_)

# All Students
@app.route('/student')
def student():
	student_ = students.find({})
	return dumps(student_)

# All Appointments
@app.route('/appointment')
def appointment():
	appointment_ = appointments.find({})
	return dumps(appointment_)


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

