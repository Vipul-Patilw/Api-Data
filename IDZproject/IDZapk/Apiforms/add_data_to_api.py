from django import forms
from django.core.exceptions import ValidationError
from IDZapk import  json_data
import  requests
class AddDataInApi(forms.Form):
	name = forms.CharField(label='Name',widget=forms.TextInput())
	age = forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={'type':'number'}))
	salary= forms.IntegerField(label='Salary',widget=forms.NumberInput(attrs={'type':'number'}))
	def clean(self):
		name= self.cleaned_data['name']
		age= self.cleaned_data['age']
		salary = self.cleaned_data['salary']
		json_data.json_data['employees'].append({'name':name,'age':age,'salary':salary})
		b= 0
		for i in json_data.json_data['employees']:
			b+= 1
			i['unique_key']=b