# Generated by Django 5.1.7 on 2025-03-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_alter_profile_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="photos/%Y/%m/%d/"
            ),
        ),
    ]
