# Generated by Django 4.2 on 2023-06-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0015_alter_event_plan_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='dip_activities',
            name='am_remarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dip_activities',
            name='dip_remarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='month_plan',
            name='remarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
