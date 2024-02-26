from rest_framework import serializers
from .models import Crop

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crop
        fields=['crop_id','crop_name','season_id','crop_category_id']