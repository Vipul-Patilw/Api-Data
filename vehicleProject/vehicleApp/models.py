
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Login(models.Model):
	
	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	mobile_number= models.CharField(max_length=122)
	
	username= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)

	password= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122)

	birthdate = models.DateField()

	def __str__(self):
		return self.first_name 
		
class Car(models.Model):
	
	vehicle_number = models.CharField(max_length=122)
	
	vehicle_type = models.CharField(max_length=122)
	
	vehicle_model= models.CharField(max_length=122)
	
	vehicle_description= models.CharField(max_length=122)

	def __str__(self):
		return self.vehicle_model


class Sign(models.Model):
	username  = models.CharField(max_length=122)
	Loginpassword = models.CharField(max_length=122)
	def __str__(self):
		return self.name

class ChangePassword(models.Model):
		old_password = models.CharField(max_length=122)
		new_password1= models.CharField(max_length=122)
		newpassword2 = models.CharField(max_length=122)

class Banking(models.Model):
	withdraw = models.FloatField()
	credit = models.FloatField()
	balance = models.FloatField(default=0)