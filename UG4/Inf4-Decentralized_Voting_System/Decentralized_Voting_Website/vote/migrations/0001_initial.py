# Generated by Django 4.0.1 on 2022-01-16 09:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EaElection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('registration_from', models.DateTimeField()),
                ('registration_to', models.DateTimeField()),
                ('voter_list', models.DateField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ea',
                'verbose_name_plural': 'Ea',
            },
        ),
        migrations.CreateModel(
            name='EaVoteUser',
            fields=[
                ('userid', models.UUIDField(auto_created=True, default=uuid.UUID('28de7a91-a4dd-4679-89c8-77f956049cef'), editable=False, primary_key=True, serialize=False)),
                ('public_key', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'EaUser',
                'verbose_name_plural': 'EaUser',
            },
        ),
    ]
