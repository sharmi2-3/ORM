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