# Generated by Django 3.0.7 on 2020-07-05 15:33

import storages.backends.s3boto3
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="thumbnail",
            field=models.FileField(
                blank=True,
                null=True,
                storage=storages.backends.s3boto3.S3Boto3Storage(),
                upload_to="",
            ),
        ),
    ]
