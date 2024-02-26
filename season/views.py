from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Season
from .serializer import SeasonSerializer

@api_view(['GET'])
def get_seasons(request):
    seasons = Season.objects.all()
    serializer = SeasonSerializer(seasons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_season(request):
    serializer = SeasonSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_season(request):
    season_id = request.data.get('season_id')
    season = get_object_or_404(Season, season_id=season_id)
    serializer = SeasonSerializer(season, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_season(request):
    season_id = request.data.get('season_id')
    season = get_object_or_404(Season, season_id=season_id)
    season.delete()
    return Response(status=204)

@api_view(['GET'])
def season_by_id(request):
    season_id = request.data.get('season_id')
    season = get_object_or_404(Season, season_id=season_id)
    serializer = SeasonSerializer(season)
    return Response(serializer.data)