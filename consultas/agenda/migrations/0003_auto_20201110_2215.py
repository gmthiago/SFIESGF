# Generated by Django 3.1.2 on 2020-11-11 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20201110_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='pedido_medico',
            field=models.FileField(default='', upload_to='', verbose_name='Pedido Médico'),
        ),
    ]