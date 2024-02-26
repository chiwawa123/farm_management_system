from rest_framework import serializers
from .models import LivestockWeight

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model=LivestockWeight
        fields=['livestock_weight_id','weight','measurement_date','livestock_id']