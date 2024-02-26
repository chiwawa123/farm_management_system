from django.urls import path
from . import views

urlpatterns = [
    path('get_livestockDosages/', views.get_livestockDosages, name='get_livestockDosages'),
    path('create_livestockDosage/', views.create_livestockDosage, name='create_livestockDosage'),
    path('update_livestockDosage/', views.update_livestockDosage, name='update_livestockDosage'),
    path('delete_livestockDosage/', views.delete_livestockDosage, name='delete_livestockDosage'),
    path('livestockDosage_by_id/', views.livestockDosage_by_id, name='livestockDosage_by_id'),
]