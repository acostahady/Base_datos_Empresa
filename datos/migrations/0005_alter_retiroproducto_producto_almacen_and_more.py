# Generated by Django 5.0 on 2023-12-24 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0004_retiroproducto_delete_transaccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retiroproducto',
            name='producto_almacen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datos.producto_almacen'),
        ),
        migrations.AlterField(
            model_name='retiroproducto',
            name='producto_proteccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datos.producto_proteccion'),
        ),
    ]
