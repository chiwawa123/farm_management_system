from rest_framework import serializers
from .models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipment
        fields=['equipment_id','equipment_name','purchase_date','plot_id','description','is_active']