# Generated by Django 3.0.5 on 2020-04-23 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('function_views', '0005_remove_user_facebook_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='title',
            new_name='profession',
        ),
    ]
