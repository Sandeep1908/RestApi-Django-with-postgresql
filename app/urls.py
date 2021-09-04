from django.db import router
from django.urls import path
from django.urls.conf import include
from . import views
# from rest_framework.routers import DefaultRouter

# router=DefaultRouter()
# router.register('studentapi',views.studentdata,basename='student')
urlpatterns=[ 
    # path('',include(router.urls)),
    path('',views.studentdata.as_view()),
    path('<int:id>/',views.studentdata.as_view()),
    path('admin/',views.Adminuser.as_view()),
    path('register/',views.registerApi.as_view(),name='register')
]