# Generated by Django 4.2.1 on 2023-05-04 17:26

import cloudinary.models
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255, validators=[users.models.validateImage], verbose_name='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
