from django.db import router
from django.urls import path
from django.urls.conf import include
from . import views


# Here all the views of our app to perform their specific takes

urlpatterns=[ 

    path('',views.studentdata.as_view()),
    path('<int:id>/',views.studentdata.as_view(),name='id'),
    path('admin/',views.Adminuser.as_view(),name='admin'),
    path('register/',views.registerApi.as_view(),name='register')
]