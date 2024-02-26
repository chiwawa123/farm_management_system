from django.db import models

# Create your models here.


class CropCategory(models.Model):
    crop_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    # Add other fields as per your requirements

    def __str__(self):
        return self.category_name