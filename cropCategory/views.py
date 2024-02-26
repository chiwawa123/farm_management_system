from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CropCategory
from .serializer import CropCategorySerializer

@api_view(['GET'])
def get_crop_category(request):
    cropCategory = CropCategory.objects.all()
    serializer = CropCategorySerializer(cropCategory, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_crop_category(request):
    serializer = CropCategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_crop_category(request):
    crop_category_id = request.data.get('crop_category_id')
    cropCategpry = get_object_or_404(CropCategory, crop_category_id=crop_category_id)
    serializer = CropCategorySerializer(cropCategpry, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_crop_category(request):
    crop_category_id = request.data.get('crop_category_id')
    cropCategpry = get_object_or_404(CropCategory, crop_category_id=crop_category_id)
    cropCategpry.delete()
    return Response(status=204)

@api_view(['GET'])
def cropCategory_by_id(request):
    crop_category_id = request.data.get('crop_category_id')
    cropCategpry = get_object_or_404(CropCategory, crop_category_id=crop_category_id)
    serializer = CropCategorySerializer(CropCategory)
    return Response(serializer.data)