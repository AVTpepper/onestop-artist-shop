# Generated by Django 3.2 on 2023-05-02 06:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Default Title', max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post')},
        ),
        migrations.RemoveField(
            model_name='like',
            name='created_at',
        ),
    ]
