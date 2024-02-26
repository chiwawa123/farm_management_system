from django.urls import path
from . import views

urlpatterns = [
    path('get_equipments/', views.get_equipments, name='equipment_list'),
    path('create_equipment/', views.create_equipment, name='create_equipment'),
    path('update_equipment/', views.update_equipment, name='update_equipment'),
    path('delete_equipment/', views.delete_equipment, name='delete_equipment'),
    path('equipment_by_id/', views.equipment_by_id, name='equipment_by_id'),
]