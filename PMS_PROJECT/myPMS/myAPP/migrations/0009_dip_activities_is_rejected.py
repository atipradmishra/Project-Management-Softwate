# Generated by Django 4.2 on 2023-06-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0008_dip_activities_is_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dip_activities',
            name='is_rejected',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
