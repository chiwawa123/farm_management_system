from django.urls import path
from . import views

urlpatterns = [
    path('get_livestocks/', views.get_livestocks, name='livestock_list'),
    path('create_livestock/', views.create_livestock, name='create_livestock'),
    path('update_livestock/', views.update_livestock, name='update_livestock'),
    path('delete_livestock/', views.delete_livestock, name='delete_livestock'),
    path('livestock_by_id/', views.livestock_by_id, name='livestock_by_id'),
]