# Generated by Django 5.0 on 2024-01-29 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0008_rename_stats_fighter_priors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cosmetic',
            name='primary_color',
        ),
        migrations.RemoveField(
            model_name='cosmetic',
            name='secondary_color',
        ),
        migrations.RemoveField(
            model_name='cosmetic',
            name='tertiary_color',
        ),
        migrations.AddField(
            model_name='cosmetic',
            name='color_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='priors',
            field=models.JSONField(default=dict),
        ),
    ]
