# Generated by Django 5.0.3 on 2024-04-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autherization', '0008_alter_doctor_has_requested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='has_requested',
            field=models.BooleanField(default=False),
        ),
    ]
