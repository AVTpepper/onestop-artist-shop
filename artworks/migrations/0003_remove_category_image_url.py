# Generated by Django 3.2 on 2023-04-26 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0002_auto_20230420_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image_url',
        ),
    ]