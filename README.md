# IITDost_Backend
IITDost_Backend

This is the backend for the IITDost app, which will code for all the apis which will be required for the app (along with server-side scripts for sending out push notifications). 

The link for the marvel app to understand the app flow -  https://marvelapp.com/1486bbd6 

Currently we are focussing on the 'Book an Appointment' (BoA) section of the app.

The database schema for this section can be described as follows-
//Insert schema diagram here

There are three main collections- 'Students', 'Staff', 'Appointments'. \
Students collection-\
  { \
    Student_details: //details like name, entry number etc \
    Appointments: //List of references to appointments in the 'Appointments' collection \
  } 

Staffs collection- 
{ \
  Staff_details: //details like name, department, link to img etc \
  Appointments: //List of references to appointments in the 'Appointments' collection \
} 

Appointments collection- \
{ \
  Staff: //Reference to staff \
  Student: // Reference to student \
  Statue: //  Requested|Approved|Done \
  and other relevant fields like Day,Time, Purpose \
} 


This schema can be easily extended for other sections of the app (like 'Request a document') by adding more collections and corresponding reference fields in the 'Student' and 'Staff' collections.

The APIs needed for the BoA section in the app are- 
1) Fetch department list - Returns list of departments as a JSON object required in the first screen in BoA section. 
2) Fetch staff list of department and images 
3) Fetch non available days for staff 
4) Fetch available time slots for staff 
5) Post Appointment details like Staff, Student, Day, Time, Purpose to add to database with status as 'requested'. 
6) Change appointment status  to 'approved'/'done'.  

For 1 and 2, app will query server whether the requested data has been updated or not (need to maintain a timestamp), and only update local copy if it has.  
