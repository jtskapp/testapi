# Generated by Django 2.1.3 on 2018-11-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0005_auto_20181115_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
