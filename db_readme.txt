To test on local mongodb server, make sure mongodb is installed ('sudo apt install mongodb' should work for ubuntu, although keep in mind the ubuntu repo is unofficial)
Create database 'iitdost' and run the following commands-
1. mongoimport --jsonArray --db iitdost --collection general  --file ./db_resources/departments.json                 
This adds the departments.json to 'general' collection in database.

Make sure the mongo server is running on port 27017 ('service mongodb status' should show active status)
Currently only '/api/departments/' endpoint has been tested.
