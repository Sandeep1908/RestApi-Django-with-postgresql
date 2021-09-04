from rest_framework import serializers
from .models import userdata

class useSerializer(serializers.ModelSerializer):
    class Meta:
        model=userdata
        fields=['id','name','roll','subject']
        