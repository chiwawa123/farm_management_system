from rest_framework import serializers
from .models import Livestock

class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Livestock
        fields=['livestock_id','tag','date_of_birth','breed','plot_id','is_active']