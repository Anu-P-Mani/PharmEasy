# Generated by Django 5.0.3 on 2024-04-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autherization', '0007_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='has_requested',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
