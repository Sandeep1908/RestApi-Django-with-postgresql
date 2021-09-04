from rest_framework import serializers
from .models import userdata


#This is Serilizer class which use userdata model
class useSerializer(serializers.ModelSerializer):
    class Meta:
        model   = userdata
        fields  = ['id','name','roll','subject']
        