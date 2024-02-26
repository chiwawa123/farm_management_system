from django.db import models

from farmer.models import Farmer

class Plot(models.Model):
    plot_id = models.AutoField(primary_key=True)
    plot_name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    # Add more fields as needed

    def __str__(self):
        return self.plot_name