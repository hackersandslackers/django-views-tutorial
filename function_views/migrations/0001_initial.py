# Generated by Django 3.0.5 on 2020-04-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("avatar", models.CharField(max_length=250, null=True)),
                ("website", models.URLField()),
                ("created_at", models.DateTimeField()),
            ],
        ),
    ]
