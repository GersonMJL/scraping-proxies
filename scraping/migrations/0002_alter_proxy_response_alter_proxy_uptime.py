# Generated by Django 4.0.2 on 2022-02-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy',
            name='response',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='proxy',
            name='uptime',
            field=models.CharField(max_length=255),
        ),
    ]
