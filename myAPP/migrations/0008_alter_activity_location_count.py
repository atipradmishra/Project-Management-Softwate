# Generated by Django 4.2 on 2024-05-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0007_dip_activities_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_location',
            name='count',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
