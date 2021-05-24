# college_attendance
Django web app to enter and monitor college attendance.  

## Important- Read these instructions before using this program for the first time
1. Clone this repo:
`git clone college_attendance`  

2. Install requirements:  
`pip install -r requirements.txt`
3. Set up the database by running the following commands:  
`py manage.py makemigrations`  

`py manage.py migrate`

4. Now, we can initialise the time table. To run the application,  
`python3 manage.py runserver`  

5. Navigate to 'Add courses' and add all the courses that you need to attend, one by one. Theory and practical has to be added separately (for example, OS and OS Lab, etc.). The attendance will also be computed separately. For people who are interested in the working, this step creates a phantom attendance record in 1995 into the database. The course can also be added in the admin site without creating this phantom record.

6. Now navigate to 'Change Time table' and enter your time table. Please note that you can only enter a maximum of 6 classes per day. If anyone can figure out a way to automate number of classes per day, in the templates, etc. a PR would be much appreciated. Hit the submit button when completed.

7. Go to 'view time table' to verify the time table entered in the database, in a read-only format.


8. You may now enter the attendance per day by clicking on the 'Modify Attendance' link. The default date selected is the most recent working day for which attendance hasn't been entered. Click 'Ok' when the date is selected. The selected date shows up in bold below the date picker. Pay no attention to the date picker after the date has been selected. The default classes entered below are as per the time table entered previously. However, even these can be changed, in case teachers have made a substitution in the class order. You have 3 options- Present, absent and not scheduled- for the cases when class should have been there but was not conducted (perhaps due to the teacher being absent). These don't count in the numerator or denominator while calculating attendance. Hit submit.  


9. Hit 'check current attendance' to see your current attendance. An attendance below 75% is shown in red. 


10. To check daywise attendance as entered in database, hit 'View detailed daywise attendance'.

11. **Please note that there is no way to remove courses already entered in step 4 via the app. To do this, either delete the file db.sqlite3 generated in step 3 present in the root directory of this repo and start adding courses from scratch- this would delete ALL of your entered attendance data; or via the admin site.**
