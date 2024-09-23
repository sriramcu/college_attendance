from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('p', 'Present'),
    ('a', 'Absent'),
    ('n', 'Not scheduled (or) cancelled')
)


class Attendance(models.Model):
    date = models.DateField()
    class_num = models.CharField(max_length=40)
    subject_name = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    comments = models.CharField(max_length=100, default='', blank=True, null=True)

    class Meta:
        db_table = 'Attendance'
        verbose_name_plural = db_table
        unique_together = ('date', 'class_num',)


class Timetable(models.Model):
    day = models.CharField(max_length=40)
    class_num = models.CharField(max_length=40)
    subject_name = models.CharField(max_length=40)

    class Meta:
        db_table = 'Timetable'
        verbose_name_plural = db_table
        unique_together = ('day', 'class_num',)
