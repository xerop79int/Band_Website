# Generated by Django 4.2.5 on 2023-11-04 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_date_venue_city_venue_contact_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sets',
            name='venue',
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('facebook_event', models.CharField(blank=True, max_length=200, null=True)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.venue')),
            ],
        ),
    ]
