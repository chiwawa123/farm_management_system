from django.urls import path
from . import views

urlpatterns = [
    path('get_seasons/', views.get_seasons, name='get_seasons'),
    path('create_season/', views.create_season, name='create_season'),
    path('update_season/', views.update_season, name='update_season'),
    path('delete_season/', views.delete_season, name='delete_season'),
    path('season_by_id/', views.season_by_id, name='season_by_id'),
]