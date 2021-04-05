from django.contrib import admin

# Register your models here.

from .models import Attendance, Timetable

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    pass
