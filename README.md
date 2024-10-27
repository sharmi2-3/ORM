# Ex02 Django ORM Web Application
## Date: 26.10.24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
...
.admin.py

from django.contrib import admin
from .models import BankLoan,BankLoanAdmin
admin.site.register(BankLoan,BankLoanAdmin)

models.py
from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
   Name=models.CharField(max_length=8)
   Accountno=models.IntegerField(primary_key="Accountno")
   age=models.IntegerField()
   Income=models.IntegerField()			
   Loanamount=models.IntegerField()
class BankLoanAdmin(admin.ModelAdmin):
   list_display=('Name','Accountno','age','Income','Loanamount')
...


## OUTPUT
![alt text](<Screenshot 2024-10-26 220215.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
