from django.urls import path
from . import views

urlpatterns = [
    path('get_plots/', views.get_plots, name='plot_list'),
    path('create_plot/', views.create_plot, name='create_plot'),
    path('update_plot/', views.update_plot, name='update_plot'),
    path('delete_plot/', views.delete_plot, name='delete_plot'),
    path('plot_by_id/', views.plot_by_id, name='plot_by_id'),
]