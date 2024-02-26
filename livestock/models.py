from django.db import models

from plot.models import Plot

class Livestock(models.Model):
    livestock_id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    plot_id = models.ForeignKey(Plot, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    # Add other fields as per your requirements

    def __str__(self):
        return self.tag