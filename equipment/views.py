from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Equipment
from .serializer import EquipmentSerializer

@api_view(['GET'])
def get_equipments(request):
    equipments = Equipment.objects.all()
    serializer = EquipmentSerializer(equipments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_equipment(request):
    serializer = EquipmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_equipment(request):
    equipment_id = request.data.get('equipment_id')
    equipment = get_object_or_404(Equipment, equipment_id=equipment_id)
    serializer = EquipmentSerializer(equipment, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_equipment(request):
    equipment_id = request.data.get('equipment_id')
    equipment = get_object_or_404(Equipment, equipment_id=equipment_id)
    equipment.delete()
    return Response(status=204)

@api_view(['GET'])
def equipment_by_id(request):
    equipment_id = request.data.get('equipment_id')
    equipment = get_object_or_404(Equipment, equipment_id=equipment_id)
    serializer = EquipmentSerializer(equipment)
    return Response(serializer.data)