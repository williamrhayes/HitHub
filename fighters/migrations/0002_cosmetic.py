# Generated by Django 5.0 on 2023-12-12 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosmetic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[('HAIR', 'HAIR'), ('EYE', 'EYE'), ('EAR', 'EAR'), ('BEARD', 'BEARD'), ('MOUTH', 'MOUTH'), ('NECK', 'NECK'), ('BODY', 'BODY'), ('ARM', 'ARM'), ('GLOVES', 'GLOVES'), ('SHORTS', 'SHORTS'), ('LEG', 'LEG'), ('FEET', 'FEET'), ('TATTOO', 'TATTOO')], max_length=8)),
                ('rarity', models.CharField(choices=[('C', 'COMMON'), ('U', 'UNCOMMON'), ('R', 'RARE'), ('E', 'EXOTIC'), ('L', 'LEGENDARY')], default='C', max_length=1)),
                ('color_shift_r', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('color_shift_g', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('color_shift_b', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('img', models.ImageField(upload_to='')),
                ('metadata', models.JSONField(null=True)),
            ],
        ),
    ]
