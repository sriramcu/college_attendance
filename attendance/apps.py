import csv
import sqlite3

from django.apps import AppConfig


class AttendanceConfig(AppConfig):
    name = 'attendance'

    def ready(self):
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
