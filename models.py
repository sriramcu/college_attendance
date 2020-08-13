from web_attendance import db

class Attendance(db.Model):
    __tablename__ = 'attendance'

    date = db.Column(db.Date, primary_key=True)
    first_class = db.Column(db.String)
    first_status = db.Column(db.String)
    second_class = db.Column(db.String)
    second_status = db.Column(db.String)
    third_class = db.Column(db.String)
    third_status = db.Column(db.String)
    fourth_class = db.Column(db.String)
    fourth_status = db.Column(db.String)
    fifth_class = db.Column(db.String)
    fifth_status = db.Column(db.String)
    sixth_class = db.Column(db.String)
    sixth_status = db.Column(db.String)
    comments = db.Column(db.String)
    
db.create_all()
    
'''
class Subject(db.Model):
    __tablename__ = 'subject'
    
    student_usn = db.Column(db.String, db.ForeignKey(Student.usn),primary_key=True)
    usn_rel = db.relationship(Student)
    course_code = db.Column(db.String,primary_key=True)
    grade = db.Column(db.String)
    
'''
