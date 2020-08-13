from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

# class AttendanceForm(FlaskForm)
#    def __init__(timetable):
#        self.first_class = S
#        super(??).__init__()

class AttendanceForm(FlaskForm):
    first_class = SelectField("1. ",coerce=str)
    first_class_status =  SelectField(coerce=str)
    
    second_class = SelectField("2. ",coerce=str)
    second_class_status =  SelectField(coerce=str)
    
    third_class = SelectField("3. ",coerce=str)
    third_class_status =  SelectField(coerce=str)
   
    fourth_class = SelectField("4. ",coerce=str)
    fourth_class_status =  SelectField(coerce=str)
    
    fifth_class = SelectField("5. ",coerce=str)
    fifth_class_status =  SelectField(coerce=str)
    
    sixth_class = SelectField("6. ",coerce=str)
    sixth_class_status =  SelectField(coerce=str)
    comments = StringField("Comments")
    submit = SubmitField("Update attendance Log")


class DateForm(FlaskForm):
    date_str = StringField("Enter date in the format DD-MM-YYYY")
    submit = SubmitField("Enter date")
