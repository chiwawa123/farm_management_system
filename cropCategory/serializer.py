from rest_framework import serializers
from .models import CropCategory

class CropCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CropCategory
        fields=['crop_category_id','category_name']