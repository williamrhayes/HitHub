# Generated by Django 5.0 on 2024-02-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0013_alter_cosmetic_color_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosmetic',
            name='type',
            field=models.CharField(choices=[('BASE', 'Base'), ('HAT', 'Hat'), ('HAIR', 'Hair'), ('EYE', 'Eyes'), ('EAR', 'Ears'), ('BEARD', 'Beard'), ('MOUTH', 'Mouth'), ('NECK', 'Neck'), ('BODY', 'Body'), ('ARM', 'Arms'), ('GLOVES', 'Gloves'), ('SHORTS', 'Shorts'), ('LEG', 'Legs'), ('FEET', 'Feet'), ('TATTOO', 'Tattoos')], max_length=8),
        ),
    ]