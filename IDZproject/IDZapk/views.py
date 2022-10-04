from django.shortcuts import redirect, render
from IDZapk.models import  UserRegistration
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserCreateForm,UserUpdateForm
from django.views.generic.edit import CreateView,FormView
from django.views.generic import ListView,DetailView
from django.contrib.messages.views import  SuccessMessageMixin
import requests
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class UserCreate(SuccessMessageMixin,CreateView):

		model = UserRegistration
		template_name = 'registration/registration.html'
		form_class = UserCreateForm
		success_url = reverse_lazy('usersdetail')
		success_message = "<strong>%(first_name)s %(last_name)s</strong> Your Details Are Submitted  Successfully"
		def form_valid(self, form):
			email = form.cleaned_data['email']
			password= form.cleaned_data['password']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			myuser = User.objects.create_user(email,email,password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.save()
			return super(UserCreate, self).form_valid(form)

class UsersDetail(ListView):
	
	model = UserRegistration
	template_name = 'usersdetail.html'
	ordering = ['-last_updated_date']
	paginate_by = 6

class UserUpdateView(UpdateView):
	template_name = 'registration/userupdate.html'
	model = UserRegistration
	form_class = UserUpdateForm
	success_url = '/usersdetail'
	
class UserDeleteView(SuccessMessageMixin,DeleteView):
	template_name = 'registration/userdelete.html'
	model = UserRegistration
	success_url = reverse_lazy('usersdetail')
	success_message = "The User has been deleted"

	
class JsonData(LoginRequiredMixin,TemplateView):
	template_name = 'jsondata.html'
	r = requests.get('http://aamras.com/dummy/EmployeeDetails.json')
	json_data = r.json()
	extra_context = {'json_data':json_data}

class JsonDetail(LoginRequiredMixin,TemplateView):
	template_name = 'jsondetail.html'
	def get_context_data(self, *args,**kwargs):
		context = super(JsonDetail, self).get_context_data(*args,**kwargs)
		r = requests.get('http://aamras.com/dummy/EmployeeDetails.json')
		json_data = r.json()
		for i in json_data['employees']:
				if i['name'] == kwargs['name']:
					context = i
		return {'jsondetail':context}

class changePassword(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')

def password_success(request):
	messages.info(request,"Password Changed Successfully")
	return render (request, 'personalDetails.html')

