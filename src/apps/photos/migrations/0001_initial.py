# Generated by Django 3.1.1 on 2020-09-18 10:23

import storages.backends.s3boto3
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Photos",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_country", models.CharField(max_length=100)),
                (
                    "photo",
                    models.FileField(
                        storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=""
                    ),
                ),
                ("url", models.CharField(max_length=100)),
            ],
        ),
    ]
