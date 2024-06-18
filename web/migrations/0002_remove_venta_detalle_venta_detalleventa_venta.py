# Generated by Django 5.0.4 on 2024-06-16 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='detalle_venta',
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.venta'),
            preserve_default=False,
        ),
    ]