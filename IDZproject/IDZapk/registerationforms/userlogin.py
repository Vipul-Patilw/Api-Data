from IDZapk.models import UserRegistration
import re
import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):
	
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'type':'password'}))
	confirm_password = forms.CharField(label=' Re-enter Password',widget=forms.PasswordInput(attrs={'type':'password'}))
	
	class Meta:
		model = UserRegistration
		fields = '__all__'
		exclude = ('last_updated_date',)
		date = datetime.date.today()
		labels = {
		'first_name': 'First Name',
		
		'last_name':'Last Name',
		
		'mobile_number':'Mobile Number',
			
		'email':'Email',
	
		'birthdate':'Birthdate'
	}
		widgets = {
			'birthdate':forms.DateInput(attrs={'type':'date','max':date}),
			'mobile_number':forms.NumberInput(attrs={'type':'number','maxlength':10}),
			'email':forms.EmailInput(attrs={'type':'email'}),		
	}
	
	def clean(self):
	
			mobile_number= self.cleaned_data['mobile_number']
			email = self.cleaned_data['email']
			password= self.cleaned_data['password']
			password2 = self.cleaned_data['confirm_password']	
			
			if len(mobile_number) != 10:
				raise ValidationError({'mobile_number':"please enter a valid 10 digit number"})
				
			if User.objects.filter(email=email):
						raise ValidationError({'email':"this email address already registered with us try different email address"})
				
			if len(password)>=6 and re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and re.search(r"[@_!#$%^&*()?/}{~:]",password) and re.search(r"[0-9]",password):
				pass
				
			else:
				raise ValidationError({'password':"password should be at least 6 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)"})
				
			if password != password2:
				raise ValidationError({'confirm_password':"confirm password doesn't matched with the password"})	

	
		
			