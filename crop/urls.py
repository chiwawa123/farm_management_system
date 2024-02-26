from django.urls import path
from . import views

urlpatterns = [
    path('get_crops/', views.get_crops, name='crop_list'),
    path('create_crop/', views.create_crop, name='create_crop'),
    path('update_crop/', views.update_crop, name='update_crop'),
    path('delete_crop/', views.delete_crop, name='delete_crop'),
    path('crop_by_id/', views.crop_by_id, name='crop_by_id'),
]