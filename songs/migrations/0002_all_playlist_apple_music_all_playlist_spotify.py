# Generated by Django 2.2.10 on 2020-04-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Playlist_Apple_Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pla_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='All_Playlist_Spotify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pla_name', models.CharField(max_length=100)),
            ],
        ),
    ]
