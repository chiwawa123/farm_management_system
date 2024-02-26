from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Farmer
from .serializer import FarmerSerializer

class FarmerView(APIView):
    def get(self, request):
        farmers = Farmer.objects.all()
        serializer = FarmerSerializer(farmers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request):
        farmer_id = request.data['id']
        farmer = get_object_or_404(Farmer, id=farmer_id)
        serializer = FarmerSerializer(farmer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        farmer_id = request.data['id']
        farmer = get_object_or_404(Farmer, id=farmer_id)
        farmer.delete()
        return Response(status=204)