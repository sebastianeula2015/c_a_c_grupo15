# Generated by Django 5.0.4 on 2024-06-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_venta_detalle_venta_detalleventa_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]