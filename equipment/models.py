from django.db import models
from plot.models import Plot

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=100)
    description = models.TextField()
    plot_id = models.ForeignKey(Plot, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    is_active = models.BooleanField(default=True)
    # Add other fields as per your requirements

    def __str__(self):
        return self.equipment_name
    
