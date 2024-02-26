from django.urls import path
from . import views

urlpatterns = [
    path('get_crop_category/', views.get_crop_category, name='get_crop_category'),
    path('create_crop_category/', views.create_crop_category, name='create_crop_category'),
    path('update_crop_category/', views.update_crop_category, name='update_crop_category'),
    path('delete_crop_category/', views.delete_crop_category, name='delete_crop_category'),
    path('cropCategory_by_id/', views.cropCategory_by_id, name='cropCategory_by_id'),
]