from django import forms
from .models import Attendance, Timetable
from bootstrap_datepicker_plus import DatePickerInput
import datetime

#widgets = {'date': DatePickerInput(format='%d/%m/%Y')}

class DateForm(forms.Form):
    date = forms.DateField(widget = forms.SelectDateWidget,initial=datetime.date.today)
 
    
