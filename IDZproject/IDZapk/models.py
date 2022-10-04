from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class UserRegistration(models.Model):
	
	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	mobile_number= models.CharField(max_length=100)
		
	email= models.CharField(max_length=122)
	
	birthdate = models.DateField()
	
	last_updated_date = models.DateTimeField(auto_now=True) #auto_now used for last_updated_date and #auto_now_add used for created_date 


	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class UserLogin(models.Model):
	username  = models.CharField(max_length=122)
	Loginpassword = models.CharField(max_length=122)
	def __str__(self):
		return self.username

class ChangePassword(models.Model):
		old_password = models.CharField(max_length=122)
		new_password1= models.CharField(max_length=122)
		newpassword2 = models.CharField(max_length=122)


