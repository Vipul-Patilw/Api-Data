#pylint:disable=E0001
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import changePassword
urlpatterns = [
   path('user/registration',views.UserCreate.as_view(), name='user-registration'),
   path('',views.UsersDetail.as_view(), name='usersdetail'),
   path('usersdetail',views.UsersDetail.as_view(), name='usersdetail'),
#   path('login',views.sign, name='login'),
   path('pass',changePassword.as_view(template_name='changePassword.html')),
   path('password_success',views.password_success, name='password_success'),
    path('api_data',views.JsonData.as_view(), name='json_data'),
 #   path('<name>',views.jsondetail, name='jsondetail'),
    path('api_data/<name>',views.JsonDetail.as_view(), name='jsondetail'),
    path('update/<pk>',views.UserUpdateView.as_view(), name='update'),
    path('delete/<pk>',views.UserDeleteView.as_view(), name='delete'),

   #path('logout',views.logoutuser, name='logout'),

]

