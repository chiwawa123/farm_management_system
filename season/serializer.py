from rest_framework import serializers
from .models import Season


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['season_id','season_name','start_date','end_date','plot_id']