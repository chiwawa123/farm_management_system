# Generated by Django 5.0.2 on 2024-02-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropCategory',
            fields=[
                ('crop_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
    ]
