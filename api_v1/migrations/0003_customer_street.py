# Generated by Django 2.1.3 on 2018-11-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_auto_20181114_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
