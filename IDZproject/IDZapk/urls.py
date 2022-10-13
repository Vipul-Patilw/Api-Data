#pylint:disable=E0001
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from IDZapk.views import UserViewSet
from django.contrib.auth import views as auth_views
from . import views
from .views import changePassword

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
   #for mobile Application
   path('mobile-app', include(router.urls)),
   #for web application
   path('user/registration',views.UserCreate.as_view(), name='user-registration'),
   path('',views.UsersDetail.as_view(), name='usersdetail'),
   path('usersdetail',views.UsersDetail.as_view(), name='usersdetail'),
   path('add_api',views.ApiAdd.as_view(), name='add-api'),
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

