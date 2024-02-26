from django.db import models

from plot.models import Plot


# Create your models here.

class Season(models.Model):
    season_id = models.AutoField(primary_key=True)
    season_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    plot_id = models.ForeignKey(Plot, on_delete=models.CASCADE)
    # Add other fields as per your requirements

    def __str__(self):
        return self.season_name