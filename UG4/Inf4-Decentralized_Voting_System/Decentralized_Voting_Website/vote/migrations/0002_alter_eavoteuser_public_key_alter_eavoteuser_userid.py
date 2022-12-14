# Generated by Django 4.0.1 on 2022-01-16 10:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eavoteuser',
            name='public_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='eavoteuser',
            name='userid',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('7a150fcf-bdd9-4097-a064-c24c6b49ca0e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
