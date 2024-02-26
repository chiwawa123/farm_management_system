from django.db import models
from django.conf import settings

class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Add other fields specific to the Farmer model
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    

    # Add more fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"