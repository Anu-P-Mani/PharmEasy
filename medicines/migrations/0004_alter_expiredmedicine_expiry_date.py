# Generated by Django 5.0.3 on 2024-04-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0003_expiredmedicine_delete_expirylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiredmedicine',
            name='expiry_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]