# Generated by Django 3.2.6 on 2021-08-29 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0003_user_rol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='user',
        ),
    ]
