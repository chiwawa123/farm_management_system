from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Crop
from .serializer import CropSerializer

@api_view(['GET'])
def get_crops(request):
    crops = Crop.objects.all()
    serializer = CropSerializer(crops, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_crop(request):
    serializer = CropSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_crop(request):
    crop_id = request.data.get('crop_id')
    crop = get_object_or_404(Crop, crop_id=crop_id)
    serializer = CropSerializer(crop, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_crop(request):
    crop_id = request.data.get('crop_id')
    crop = get_object_or_404(Crop, crop_id=crop_id)
    crop.delete()
    return Response(status=204)

@api_view(['GET'])
def crop_by_id(request):
    crop_id = request.data.get('crop_id')
    crop = get_object_or_404(Crop, crop_id=crop_id)
    serializer = CropSerializer(crop)
    return Response(serializer.data)