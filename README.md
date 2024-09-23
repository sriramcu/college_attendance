# Django Monitor College Attendance
Django web app to enter and monitor college attendance.  

Handles cases where classes are rescheduled or cancelled. Also handles cases where 
the class was taken but the teacher forgot to take attendance.

## Instructions
1. Install SQLite on your system. <br><br>
2. Clone the repo and install requirements:  
`pip install -r requirements.txt` <br><br>
3. Set up the database by running the following commands:  
    <br>
    `python manage.py makemigrations`  
    
    `python manage.py migrate`

4. Now, we can initialise the time table. To run the application,  
`python manage.py runserver`  

5. Navigate to '**Add courses**', and add all the courses that you need to attend, one by 
   one. Theory and practical has to be added separately (for example, OS and OS Lab, 
   etc.). The attendance will also be computed separately. For people who are 
   interested in the working, this step creates a phantom attendance record in 1995 
   into the database in order to avoid division by zero error. The course can also be 
   added in the admin site without creating this phantom record. Once entered, these 
   values cannot be changed except via the admin site, or deleting the db and starting 
   from step 1.
<br><br>
6. Now navigate to 'Change **Time table**' and enter your time table. Please note that 
   you can only enter a maximum of 6 classes per day. Hit the submit button when completed.
<br><br>
7. Go to 'view time table' to verify the time table entered in the database, in a read-only format.
<br><br>
8. You may now **enter the attendance per day** by clicking on the 'Modify Attendance' 
   link. The default date selected is the most recent working day for which attendance 
   hasn't been entered. 
<br><br>
9. Click 'Ok' when the date is selected. The selected date shows up in bold below the 
   date picker. Pay no attention to the date picker after the date has been selected. 
   <br><br>
10. The default classes can be seen below the date picker. These default values 
    correspond to the time table entered in step 6 ("change timetable"). The actual 
    classes can be changed from their default value using the drop-down menus. This is 
    to handle situations where teachers have made a substitution or cancellation. You 
    have 3 options- Present, absent and not scheduled (not counted as a class at all, 
    so not factored into the attendance percentage).
<br><br>
10. Hit '**check current attendance**' to see your current attendance. An attendance below 
    75% is shown in red. 
<br><br>
11. To check day-wise attendance as entered in database, click on 'View detailed daywise 
attendance'.