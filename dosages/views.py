from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LivestockDosage
from .serializer import DosageSerializer

@api_view(['GET'])
def get_livestockDosages(request):
    livestockDosages = LivestockDosage.objects.all()
    serializer = DosageSerializer(livestockDosages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_livestockDosage(request):
    serializer = DosageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_livestockDosage(request):
    livestockDosage_id = request.data.get('livestockDosage_id')
    livestockDosage = get_object_or_404(LivestockDosage, livestockDosage_id=livestockDosage_id)
    serializer = DosageSerializer(LivestockDosage, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_livestockDosage(request):
    livestockDosage_id = request.data.get('livestockDosage_id')
    livestockDosage = get_object_or_404(LivestockDosage, livestockDosage_id=livestockDosage_id)
    livestockDosage.delete()
    return Response(status=204)

@api_view(['GET'])
def livestockDosage_by_id(request):
    livestockDosage_id = request.data.get('livestockDosage_id')
    livestockDosage = get_object_or_404(LivestockDosage, livestockDosage_id=livestockDosage_id)
    serializer = DosageSerializer(livestockDosage)
    return Response(serializer.data)