# Generated by Django 5.0.3 on 2024-05-29 06:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_rename_is_avail_booking_is_available'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='department',
            field=models.CharField(choices=[('Cardiology', 'Cardiology'), ('Orthopedics', 'Orthopedics'), ('Neurology', 'Neurology'), ('Oncology', 'Oncology'), ('Pediatrics', 'Pediatrics'), ('Gynecology', 'Gynecology'), ('Dermatology', 'Dermatology'), ('Psycology', 'Psycology')], default='Cardiology', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='booking',
            name='is_available',
        ),
    ]