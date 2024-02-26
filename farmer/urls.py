from django.urls import path
from .views import FarmerView

urlpatterns = [
    path('farmers/', FarmerView.as_view()),
]