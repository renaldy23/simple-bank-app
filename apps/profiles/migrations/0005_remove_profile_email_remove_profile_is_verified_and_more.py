# Generated by Django 5.1.7 on 2025-04-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0004_profile_photo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="is_verified",
        ),
        migrations.AlterField(
            model_name="profile",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
