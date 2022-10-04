from IDZapk.models import UserRegistration
import datetime
from django import forms
from django.core.exceptions import ValidationError

class UserUpdateForm(forms.ModelForm):

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
			if len(mobile_number) != 10:
				raise ValidationError({'mobile_number':"please enter a valid 10 digit number"})
				
		
			