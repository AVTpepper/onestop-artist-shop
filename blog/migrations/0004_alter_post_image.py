# Generated by Django 3.2 on 2023-05-03 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230502_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.png', upload_to='posts/'),
        ),
    ]