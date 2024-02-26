from rest_framework import serializers
from .models import Farmer

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Farmer
        fields=['farmer_id','first_name','last_name','gender','age','phone_number','user_id','address']

        