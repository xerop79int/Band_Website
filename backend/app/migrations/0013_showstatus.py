# Generated by Django 4.2 on 2023-06-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_playlist_number_remove_playlist_set_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_show_started', models.BooleanField(default=False)),
            ],
        ),
    ]
