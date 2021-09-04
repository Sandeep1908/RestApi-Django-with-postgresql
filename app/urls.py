from django.db import router
from django.urls import path
from django.urls.conf import include
from . import views


# Here all the views of our app to perform their specific takes

urlpatterns=[ 

    #This url helps to show all data
    path('',views.studentdata.as_view()),
    #This url helps to show data of one user
    path('<int:id>/',views.studentdata.as_view(),name='id'),
    #This url is used to admin user only
    path('admin/',views.AdminuserApi.as_view(),name='admin'),
    #This url helps to create user 
    path('register/',views.registerApi.as_view(),name='register'),
    #This url help to recover password
    path('forgotapi/',views.ForgotApi.as_view(),name='forgot')
]