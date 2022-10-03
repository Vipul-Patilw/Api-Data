
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import changePassword
urlpatterns = [
   path('sign',views.index, name='sign'),
   path('logininfo.html',views.index, name='sign'),
   path('login',views.sign, name='login'),
   path('index.html',views.sign, name='login'),
   path('carDetail',views.carDetail, name='carDetail'),
   path('carCreate',views.carCreate, name='carCreate'),
   path('',views.carDetail, name='carDetail'),
   path('pass.html',changePassword.as_view(template_name='changePassword.html')),
   path('password_success',views.password_success, name='password_success'),
   path('personalDetails.html',views.personalDetails, name='personalDetails'),
  path('adminlogin',views.adminlogin, name='admin'),
  path('adminsignIn',views.adminsign, name='adminsign'),
  path('request',views.request, name='request'),
   path('deleteVehicle',views.deleteVehicle, name='deleteVehicle'),
  path('updateVehicle',views.updateVehicle, name='updateVehicle'),
   path('logout',views.logoutuser, name='logout'),
   path('gg',views.creditwithdraw, name='gg'),

]

