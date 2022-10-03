
from django.shortcuts import redirect, render
from vehicleApp.models import  Login,Car,Banking
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from vehicleProject import settings

# Create your views here.

class changePassword(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')

def password_success(request):
	messages.info(request,"Password Changed Successfully")
	return render (request, 'personalDetails.html')

def carDetail(request):
	carDetails = Car.objects.all()
	if request.method =="POST":
			vehicle_number = request.POST.get('vehicle_number')
			vehicle = Car.objects.filter(vehicle_number=vehicle_number).all()
			return render(request,'updateVehicleDetail.html',
			{'vehicles':vehicle})

	return render (request,'carDetail.html',{'carDetail':carDetails})

def updateVehicle(request):
	if request.method =="POST":
		vehicle_number = request.POST.get('vehicle_number')
		vehicle_type = request.POST.get('vehicle_type')
		vehicle_model = request.POST.get('vehicle_model')
		vehicle_description = request.POST.get('vehicle_description')
	
		vehicleDetail = Car.objects.get(vehicle_number=vehicle_number)
		
		vehicleDetail.vehicle_type=vehicle_type
		vehicleDetail.vehicle_model=vehicle_model
		vehicleDetail.vehicle_description=vehicle_description
		vehicleDetail.vehicle_number=vehicle_number
		vehicleDetail.save()

		return  redirect('/carDetail')

	return render(request,'updateVehicleDetail.html')

def deleteVehicle(request):
	if request.method =="POST":
			vehicle_number = request.POST.get('vehicle_number')
			box = request.POST.get('box')
			add = Car.objects.all()
			if box == "on":
				vehicle = Car.objects.get(vehicle_number=vehicle_number)
				vehicle.delete()
				messages.success(request,"Vehicle Deleted succesfully")
			return redirect('/deleteVehicle',{'carDetail':add})
	add = Car.objects.all()
	return render(request,'deletevehicle.html',{'carDetail':add})
	
	
			
def carCreate(request):
	if request.method =="POST":
		vehicle_number = request.POST.get('vehicle_number')
		vehicle_type = request.POST.get('vehicle_type')
		vehicle_model = request.POST.get('vehicle_model')
		vehicle_description = request.POST.get('vehicle_description')
	
		vehicleDetail = Car(vehicle_number=vehicle_number,vehicle_type=vehicle_type,vehicle_model=vehicle_model,vehicle_description=vehicle_description)
		vehicleDetail.save()

		return  redirect('/carDetail')
	return render (request, 'carCreate.html')

def creditwithdraw(request):
	if request.method =="POST":
		withdraw = request.POST.get('withdraw')
		credit = request.POST.get('credit')
		dd = Banking.objects.all()
		dd.balance -= withdraw
		dd.balance += credit
		dd.save()

		return  redirect('/gg')
	return render (request, 'gg.html')
	
def index(request):
		if request.method =="POST":
		
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			mobile_number= request.POST.get('mobile_number')
			username= request.POST.get('username')
			email = request.POST.get('email')
			password= request.POST.get('password')
			gender = request.POST.get('gender')
			birthdate = request.POST.get('birthdate')
			password2 = request.POST.get('password2')
			
		
			if User.objects.filter(email=email):
						messages.error(request,"this email address already registered with us try different email address")
						return redirect("/sign")
						
			if User.objects.filter(username=username):
						messages.error(request,"this username is already exist try another")
						return redirect("/sign")

			if password != password2:
				messages.error(request,"confirm password doesn't matched with the password")
				return redirect ('/sign')
				
			if len(password)>=6 and re.search(r"[A-Z][a-z]",password) and re.search(r"[@_!#$%^&*()?/}{~:]",password) and re.search(r"[0-9]",password):
				pass
				
			else:
				messages.error(request,"password should be at least 6 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)")
				return redirect("/sign")
				

			messages.success(request, first_name.title() + " " + last_name.title())
			myuser = User.objects.create_user(username,password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.is_active = False
			myuser.save()	
			
			users = Login(first_name=first_name,username=username, mobile_number=mobile_number,last_name=last_name,email=email,birthdate=birthdate,gender=gender,)
			users.save()		

			return redirect('/login')

		return render(request, 'logininfo.html')
	
	#  return HttpResponse("vipul patil")
def adminsign(request):
		if request.method =="POST":
		
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			username= request.POST.get('username')
			email = request.POST.get('email')
			password= request.POST.get('password')
			password2 = request.POST.get('password2')
			
		
			if User.objects.filter(email=email):
						messages.error(request,"this email address already registered with us try different email address")
						return redirect("/adminsignIn")
						
			if User.objects.filter(username=username):
						messages.error(request,"this username is already exist try another")
						return redirect("/adminsignIn")

			if password != password2:
				messages.error(request,"confirm password doesn't matched with the password")
				return redirect ('/adminsignIn')
				
			if len(password)>=6 and re.search(r"[A-Z][a-z]",password) and re.search(r"[@_!#$%^&*()?/}{~:]",password) and re.search(r"[0-9]",password):
				pass
				
			else:
				messages.error(request,"password should be at least 6 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)")
				return redirect("/adminsignIn")
				

			messages.success(request, first_name.title() + " " + last_name.title())
			myuser = User.objects.create_user(username,email,password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.save()	
			users = Staff(first_name=first_name,username=username, last_name=last_name,email=email)
			users.save()

			
			return redirect('/adminlogin')
					

		return render(request, 'adminsignIn.html')

def sign(request):

	if request.method =="POST":
		Loginpassword= request.POST.get('Loginpassword')
		username = request.POST.get('username')
		user = authenticate(username=username, password=Loginpassword)
		if user is not None:
			
			login(request, user)
			return redirect('/carDetail')
	
		else:

			messages.error(request, "Please enter correct username and  password ")
			return redirect('/login')    

	return render(request,'index.html')


def adminlogin(request):
	try:
		if request.method =="POST":
			Loginpassword= request.POST.get('Loginpassword')
			username = request.POST.get('username')
			user = authenticate(username=username, password=Loginpassword)
			
			if user is not None and user.is_superuser == True or user.is_staff == True:
				
				login(request, user)
				return redirect('/carDetail')

			elif user.is_staff == False or user.is_superuser == False:
					messages.error(request, "this account don't have accessed to login as admin , try using your admin or super admin login account!")
						
					return redirect('/adminlogin')
			

		return render(request,'Adminlogin.html')
	except:
				messages.error(request, "You enter wrong username and password")
					
				return redirect('/adminlogin')    



def personalDetails (request):
	return render (request,'personalDetails.html')

def logoutuser(request):
	logout(request)
	return redirect ("/login")

def request(request):
	if request.method =="POST" and 'user' in request.POST:
			username = request.POST.get('username')
			users = User.objects.get(username=username)
			users.is_staff = True
			users.save()
			staff = Staff.objects.get(username=username)
			staff.delete()
			messages.success(request,f"{users.first_name} {users.last_name} request for admin account accessed is accepted ")
			return redirect('/request')
	if request.method =="POST" and 'user1' in request.POST:
			username1 = request.POST.get('username1')
			users = User.objects.get(username=username1)
			staff = Staff.objects.get(username=username1)
			staff.delete()
			messages.success(request,f"{users.first_name} {users.last_name} request for admin account accessed is Rejected ")
			return redirect('/request')
	
	user = Staff.objects.all()
	return render(request,'request.html',{'users':user})


