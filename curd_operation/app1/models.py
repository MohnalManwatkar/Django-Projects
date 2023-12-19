from django.db import models

class EmployeeTable(models.Model):
    Emp_id = models.IntegerField(null=False, blank=False)
    Fname = models.CharField(max_length=50,null=False, blank=False)
    Lname = models.CharField(max_length=50,null=False, blank=False)
    Email_id = models.EmailField(max_length=50,null=False, blank=False)
    Contact = models.BigIntegerField(null=False, blank=False)
    Salary = models.IntegerField(null=False, blank=False)
    Location = models.CharField(max_length=50,null=False, blank=False)