from rest_framework import serializers
from .models import LivestockDosage


class DosageSerializer(serializers.ModelSerializer):
    class Meta:
        model=LivestockDosage
        fields=['dosage_id','livestock_id','medication','dosage_amount','dosage_unit','administration_date']