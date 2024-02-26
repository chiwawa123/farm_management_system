from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LivestockWeight
from .serializer import WeightSerializer

@api_view(['GET'])
def get_livestockWeights(request):
    livestockWeights = LivestockWeight.objects.all()
    serializer = WeightSerializer(livestockWeights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_livestockWeight(request):
    serializer = WeightSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_livestockWeight(request):
    livestockWeight_id = request.data.get('livestockWeight_id')
    livestockWeight = get_object_or_404(LivestockWeight, livestockWeight_id=livestockWeight_id)
    serializer = WeightSerializer(livestockWeight, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_livestockWeight(request):
    livestockWeight_id = request.data.get('livestockWeight_id')
    livestockWeight = get_object_or_404(LivestockWeight, livestockWeight_id=livestockWeight_id)
    livestockWeight.delete()
    return Response(status=204)

@api_view(['GET'])
def livestockWeight_by_id(request):
    livestockWeight_id = request.data.get('livestockWeight_id')
    livestockWeight = get_object_or_404(LivestockWeight, livestockWeight_id=livestockWeight_id)
    serializer = WeightSerializer(livestockWeight)
    return Response(serializer.data)