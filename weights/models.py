from django.db import models

from livestock.models import Livestock

class LivestockWeight(models.Model):
    livestock_weight_id = models.AutoField(primary_key=True)
    livestock_id = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    weight = models.FloatField()
    measurement_date = models.DateField()

    # Add other fields as per your requirements

    def __str__(self):
        return f"{self.livestock_id} - {self.weight} kg - {self.measurement_date}"