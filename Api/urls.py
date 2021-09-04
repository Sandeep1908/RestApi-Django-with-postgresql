from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('studentapi/',include('app.urls'))
    
]
