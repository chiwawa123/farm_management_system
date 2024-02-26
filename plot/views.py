from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Plot
from .serializer import PlotSerializer

@api_view(['GET'])
def get_plots(request):
    plots = Plot.objects.all()
    serializer = PlotSerializer(plots, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_plot(request):
    serializer = PlotSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_plot(request):
    pk = request.data.get('pk')
    plot = get_object_or_404(Plot, pk=pk)
    serializer = PlotSerializer(plot, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_plot(request):
    plot_id = request.data.get('plot_id')
    plot = get_object_or_404(Plot, plot_id=plot_id)
    plot.delete()
    return Response(status=204)

@api_view(['GET'])
def plot_by_id(request):
    plot_id = request.data.get('plot_id')
    plot = get_object_or_404(Plot, plot_id=plot_id)
    serializer = PlotSerializer(plot)
    return Response(serializer.data)