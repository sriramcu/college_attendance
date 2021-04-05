from django.apps import AppConfig
import os

class AttendanceConfig(AppConfig):
    name = 'attendance'
    def ready(self):
        os.system("sqlite3 -header -csv db.sqlite3 'select * from Attendance;' > out.csv")
