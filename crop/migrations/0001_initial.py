# Generated by Django 5.0.2 on 2024-02-25 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cropCategory', '0001_initial'),
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('crop_id', models.AutoField(primary_key=True, serialize=False)),
                ('crop_name', models.CharField(max_length=100)),
                ('crop_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cropCategory.cropcategory')),
                ('season_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='season.season')),
            ],
        ),
    ]
