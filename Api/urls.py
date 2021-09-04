from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# here we import some jwt classes for generating token

urlpatterns = [
    path('admin/', admin.site.urls),
    # this gettoken url hits the tokenObtainPairView class to help generting token
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    #this refresh url will help to regenerating our token again
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    # this url help to connet our apps urls
    path('studentapi/',include('app.urls'))
    
]
