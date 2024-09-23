import csv
import datetime
import sqlite3

import pandas
from django.contrib import messages
from django.shortcuts import render
from django.template.defaulttags import register

from .forms import DateForm
from .models import Attendance, Timetable


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def modify(request):
    date_obj = Attendance.objects.order_by('-date').first()
    if date_obj:
        date_obj = date_obj.date
        if date_obj.strftime("%A") == "Friday" and request.method != 'POST':
            n = 3
        elif date_obj.strftime("%A") == "Thursday" and request.method == 'POST' and 'submit' in request.POST:
            n = 4
        else:
            if request.method == 'POST' and 'submit' in request.POST:
                n = 2
            else:
                n = 1

        date_obj = date_obj + datetime.timedelta(days=n)
        date_str = date_obj.strftime("%Y-%m-%d")
    else:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    print(date_str)
    form1 = DateForm(initial={'date': date_str})

    if request.method == 'POST' and 'submit' in request.POST:
        this_day = request.session['this_day']
        dt_obj = datetime.datetime.strptime(this_day, '%d-%m-%Y')
        for i in range(1, 7, 1):
            class_key = 'class{}'.format(i)
            status_key = 'status{}'.format(i)
            subject_name = request.POST[class_key]
            status = request.POST[status_key]
            comments = request.POST['comments']
            if subject_name != '':
                Attendance.objects.update_or_create(date=dt_obj, class_num=str(i),
                                                    defaults={'subject_name': subject_name, 'status': status,
                                                              'comments': comments})

        messages.success(request, "Attendance successfully entered!")
        return render(request, 'modify.html', {'form1': form1})

    elif request.method == 'POST':
        # form1 = DateForm()
        # default = {1:'a',2:'c',3:'',4:'b',5:'',6:'a'}
        # 'date_month': ['3'], 'date_day': ['10'], 'date_year': ['2021']
        this_day = request.POST['date_day'].zfill(2) + '-' + request.POST['date_month'].zfill(2) + "-" + request.POST[
            'date_year']

        dt_obj = datetime.datetime.strptime(this_day, '%d-%m-%Y')
        today = dt_obj.strftime('%a')
        full_dayname = dt_obj.strftime('%A')
        default = {}
        for i in range(1, 7, 1):
            tt_obj = Timetable.objects.filter(day=today, class_num=i).first()
            if tt_obj:
                default[i] = tt_obj.subject_name

        classes = list(Attendance.objects.order_by().values_list('subject_name', flat=True).distinct())
        classes.insert(0, '')

        request.session['this_day'] = this_day
        date_day = request.POST['date_day']
        date_month = request.POST['date_month']
        date_year = request.POST['date_year']
        return render(request, 'modify.html',
                      {'form1': form1, 'classes': classes, 'default': default, 'dayname': full_dayname,
                       'date_day': date_day, 'date_month': date_month, 'date_year': date_year})

    return render(request, 'modify.html', {'form1': form1})


def check(request):
    classes = list(Attendance.objects.order_by().values_list('subject_name', flat=True).distinct())

    present = []
    absent = []
    total = []
    att = []
    for subject in classes:
        num_present = Attendance.objects.filter(subject_name=subject, status='p').count()
        num_absent = Attendance.objects.filter(subject_name=subject, status='a').count()
        present.append(num_present)
        absent.append(num_absent)
        total.append(num_present + num_absent)
        if total[-1] == 0:
            att.append(0)
        else:
            att.append(round((num_present) / (num_present + num_absent), 4) * 100)

    data = zip(classes, present, absent, total, att)
    return render(request, 'check.html', {'data': data})


def view_tt(request):
    num_classes = 6
    num_classes_list = [(x + 1) for x in range(num_classes)]
    tt_dict = {}
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for day in days:
        tt_dict[day] = {}
        day_tt = Timetable.objects.filter(day=day)
        if day_tt is not None:
            for cl in day_tt:
                tt_dict[cl.day][cl.class_num] = cl.subject_name

    return render(request, 'view_tt.html', {'dict': tt_dict, 'num_classes_list': num_classes_list, 'days': days})


def change_tt(request):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    num_classes = 6

    if request.method == 'POST':

        for day in days:
            for class_num in range(1, num_classes + 1):
                class_name = request.POST[day + str(class_num)]
                Timetable.objects.update_or_create(day=day, class_num=class_num, defaults={'subject_name': class_name})

        messages.success(request, "Time table updated successfully!!")

    classes = list(Attendance.objects.order_by().values_list('subject_name', flat=True).distinct())
    classes.insert(0, '')

    num_classes_list = [(x + 1) for x in range(num_classes)]
    tt_dict = {}

    for day in days:
        tt_dict[day] = {}
        day_tt = Timetable.objects.filter(day=day)
        if day_tt is not None:
            for cl in day_tt:
                tt_dict[cl.day][cl.class_num] = cl.subject_name

    return render(request, 'change_tt.html',
                  {'dict': tt_dict, 'classes': classes, 'num_classes_list': num_classes_list})


def detailed(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Attendance")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    with open('out.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(rows)
    cursor.close()
    conn.close()
    pr = pandas.read_csv('out.csv')
    s = str(pandas.DataFrame.to_html(pr))
    f = open("attendance/templates/dump.html", 'w')
    f.write('{% extends "base.html" %}\n{% block content %}')
    f.write(s)
    f.write('\n{% endblock content %}\n')
    f.close()
    return render(request, "dump.html", {})


def add_courses(request):
    if request.method == 'POST':
        att = Attendance.objects.filter(date=datetime.date(1995, 1, 1)).first()
        if att == None:
            my_num = 1

        else:
            my_num = int(
                Attendance.objects.filter(date=datetime.date(1995, 1, 1)).order_by('-class_num').first().class_num) + 1

        Attendance.objects.create(date=datetime.date(1995, 1, 1), class_num=my_num, subject_name=request.POST['course'],
                                  status='n')
        messages.success(request, "Course successfully added")

    classes = list(Attendance.objects.order_by().values_list('subject_name', flat=True).distinct())

    return render(request, "add_courses.html", {"classes": classes})


# delete from Attendance where date='1995-01-01'; to undo the above add courses

def base(request):
    return render(request, 'base.html')
