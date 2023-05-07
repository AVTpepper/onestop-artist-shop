# Generated by Django 3.2 on 2023-04-22 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artworks', '0002_auto_20230420_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    ),
                )
                ('quantity', models.PositiveIntegerField(default=1)),
                (
                    'artwork',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='artworks.artwork'
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL
                    ),
                ),

            ],
        ),
    ]
