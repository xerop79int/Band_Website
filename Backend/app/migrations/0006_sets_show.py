# Generated by Django 4.2.5 on 2023-11-04 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_sets_venue_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='sets',
            name='show',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.show'),
        ),
    ]
