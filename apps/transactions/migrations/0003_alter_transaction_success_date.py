# Generated by Django 5.1.7 on 2025-04-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0002_transaction_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="success_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
