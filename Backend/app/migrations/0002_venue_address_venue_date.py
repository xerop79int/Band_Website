# Generated by Django 4.2.5 on 2023-10-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='address',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
