from django.urls import path
from . import views

urlpatterns = [
    path('get_livestockWeights/', views.get_livestockWeights, name='get_livestockWeights'),
    path('create_livestockWeight/', views.create_livestockWeight, name='create_livestockWeight'),
    path('update_livestockWeight/', views.update_livestockWeight, name='update_livestockWeight'),
    path('delete_livestockWeight/', views.delete_livestockWeight, name='delete_livestockWeight'),
    path('livestockWeight_by_id/', views.livestockWeight_by_id, name='livestockWeight_by_id'),
]