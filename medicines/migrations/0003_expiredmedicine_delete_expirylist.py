# Generated by Django 5.0.3 on 2024-04-16 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_expirylist_expmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiredMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateTimeField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.medicine_inventory')),
            ],
        ),
        migrations.DeleteModel(
            name='Expirylist',
        ),
    ]
