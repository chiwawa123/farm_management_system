from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Livestock
from .serializer import LivestockSerializer

@api_view(['GET'])
def get_livestocks(request):
    livestocks = Livestock.objects.all()
    serializer = LivestockSerializer(livestocks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_livestock(request):
    serializer = LivestockSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_livestock(request):
    livestock_id = request.data.get('livestock_id')
    livestock = get_object_or_404(Livestock, livestock_id=livestock_id)
    serializer = LivestockSerializer(livestock, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_livestock(request):
    livestock_id = request.data.get('livestock_id')
    livestock = get_object_or_404(Livestock, livestock_id=livestock_id)
    livestock.delete()
    return Response(status=204)

@api_view(['GET'])
def livestock_by_id(request):
    livestock_id = request.data.get('livestock_id')
    livestock = get_object_or_404(Livestock, livestock_id=livestock_id)
    serializer = LivestockSerializer(livestock)
    return Response(serializer.data)