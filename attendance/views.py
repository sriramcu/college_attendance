from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Attendance,Timetable

from django.template.defaulttags import register

from .forms import DateForm

import datetime

import numpy as np

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def modify(request):
    form1 = DateForm()

    if request.method == 'POST' and 'submit' in request.POST:
        # ~ <QueryDict: {'csrfmiddlewaretoken': ['6gpAXwpCAz3LWw6Z0xuvIwyIAzmK5zKvq7W3buYqn4G5s9u2CaVTPITd1VpBLqk5'], 'class1': ['Physics'], 'status1': ['n'], 'class2': [''], 'status2': ['n'], 'class3': [''], 'status3': ['a'], 'class4': [''], 'status4': ['n'], 'class5': [''], 'status5': ['n'], 'class6': [''], 'status6': ['n'], 'submit': ['Submit']}>
        this_day = request.session['this_day']
        dt_obj = datetime.datetime.strptime(this_day, '%d-%m-%Y')
        for i in range(1,7,1):
            class_key = 'class{}'.format(i)
            status_key = 'status{}'.format(i)
            subject_name  = request.POST[class_key]
            status = request.POST[status_key]
            comments = request.POST['comments']
            if subject_name != '':
                Attendance.objects.update_or_create(date=dt_obj,class_num=str(i),defaults = {'subject_name':subject_name,'status':status,'comments':comments})
            
        messages.success(request,"Attendance successfully entered!")
        return render(request, 'modify.html',{'form1':form1})

    elif request.method == 'POST':
       
        #default = {1:'a',2:'c',3:'',4:'b',5:'',6:'a'}
        #'date_month': ['3'], 'date_day': ['10'], 'date_year': ['2021']
        this_day = request.POST['date_day'].zfill(2)+'-'+request.POST['date_month'].zfill(2)+"-"+request.POST['date_year']
        
        dt_obj = datetime.datetime.strptime(this_day, '%d-%m-%Y')
        today = dt_obj.strftime('%a')
        full_dayname = dt_obj.strftime('%A')
        default = {}
        for i in range(6):
            tt_obj = Timetable.objects.filter(day=today,class_num=i).first()
            if tt_obj:
                default[i] = tt_obj.subject_name
      
        classes = list(Timetable.objects.order_by().values_list('subject_name',flat=True).distinct())
        classes.insert(0,'')

        request.session['this_day'] = this_day
        date_day = request.POST['date_day']
        date_month = request.POST['date_month']
        date_year = request.POST['date_year']
        return render(request, 'modify.html',{'form1':form1,'classes':classes,'default':default,'dayname':full_dayname,'date_day':date_day,'date_month':date_month,'date_year':date_year})
        
    
       
    
    return render(request, 'modify.html',{'form1':form1})
    
def check(request):
    classes = list(Timetable.objects.order_by().values_list('subject_name',flat=True).distinct())
    present = []
    absent = []
    total = []
    att = []
    for subject in classes:
        num_present = Attendance.objects.filter(subject_name=subject,status='p').count()
        num_absent = Attendance.objects.filter(subject_name=subject,status='a').count()
        present.append(num_present)
        absent.append(num_absent)
        total.append(num_present+num_absent)
        if total[-1] == 0:
            att.append(0)
        else:
            att.append(round((num_present)/(num_present+num_absent),2))
    
    data = zip(classes,present,absent,total,att)
    return render(request, 'check.html',{'data':data})
    
def change_tt(request):
    num_classes = 6
    num_classes_list = [(x+1) for x in range(num_classes)]
    tt_dict = {}
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    for day in days:
        tt_dict[day] = {}
        day_tt = Timetable.objects.filter(day = day)
        if day_tt is not None:
            for cl in day_tt:
                tt_dict[cl.day][cl.class_num] = cl.subject_name
            
    
   
    return render(request, 'change_tt.html',{'dict':tt_dict,'num_classes_list':num_classes_list,'days':days})
    
def base(request):
    return render(request, 'base.html')
