from django.db import models

from cropCategory.models import CropCategory
from season.models import Season

# Create your models here.
class Crop(models.Model):
    crop_id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=100)
    crop_category_id = models.ForeignKey(CropCategory, on_delete=models.CASCADE)
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE)
    # Add other fields as per your requirements

    def __str__(self):
        return self.crop_name