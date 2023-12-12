# Generated by Django 5.0 on 2023-12-12 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0002_cosmetic'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_arm',
            field=models.ForeignKey(limit_choices_to={'type': 'ARM'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_arm', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_beard',
            field=models.ForeignKey(limit_choices_to={'type': 'BEARD'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_beard', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_body',
            field=models.ForeignKey(limit_choices_to={'type': 'BODY'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_body', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_ear',
            field=models.ForeignKey(limit_choices_to={'type': 'EAR'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_ear', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_eye',
            field=models.ForeignKey(limit_choices_to={'type': 'EYE'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_eye', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_feet',
            field=models.ForeignKey(limit_choices_to={'type': 'FEET'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_feet', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_gloves',
            field=models.ForeignKey(limit_choices_to={'type': 'GLOVES'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_gloves', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_hair',
            field=models.ForeignKey(limit_choices_to={'type': 'HAIR'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_hair', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_leg',
            field=models.ForeignKey(limit_choices_to={'type': 'LEG'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_leg', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_mouth',
            field=models.ForeignKey(limit_choices_to={'type': 'MOUTH'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_mouth', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_neck',
            field=models.ForeignKey(limit_choices_to={'type': 'NECK'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_neck', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_shorts',
            field=models.ForeignKey(limit_choices_to={'type': 'SHORTS'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_shorts', to='fighters.cosmetic'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='cosmetic_tattoo',
            field=models.ForeignKey(limit_choices_to={'type': 'TATTOO'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters_tattoo', to='fighters.cosmetic'),
        ),
    ]
