from django.db import models
from datetime import date


class Clients(models.Model):
    employee_id = models.IntegerField(default=99999999)
    employee_name = models.CharField(max_length=100)
    employee_status = models.CharField(max_length=10)
    employee_age = models.IntegerField(default=100)
    employee_ssn = models.CharField(max_length=20)
    employee_date = models.DateField(date.today)
    employee_gender = models.CharField(max_length=10)

    def __str__(self):

        return str(self.employee_id) + " - " + str(self.employee_name)







