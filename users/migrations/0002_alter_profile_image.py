# Generated by Django 5.1.4 on 2025-01-05 18:43

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics', validators=[users.models.validate_image_format]),
        ),
    ]
