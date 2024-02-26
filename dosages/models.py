from django.db import models

from livestock.models import Livestock

class LivestockDosage(models.Model):
    dosage_id = models.AutoField(primary_key=True)
    livestock_id = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    medication = models.CharField(max_length=100)
    dosage_amount = models.FloatField()
    dosage_unit = models.CharField(max_length=50)
    administration_date = models.DateField()

    # Add other fields as per your requirements

    def __str__(self):
        return f"{self.livestock_id} - {self.medication} - {self.dosage_amount} {self.dosage_unit}"