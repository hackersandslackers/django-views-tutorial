# Generated by Django 3.0.5 on 2020-04-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("function_views", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="title",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
