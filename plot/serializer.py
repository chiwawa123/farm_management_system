from rest_framework import serializers
from .models import Plot

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields=['plot_id','plot_name','farmer_id','area','location']