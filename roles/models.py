from django.db import models

class Role(models.Model):
    role_id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=255)
