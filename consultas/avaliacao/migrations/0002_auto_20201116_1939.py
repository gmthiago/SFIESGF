# Generated by Django 3.1.2 on 2020-11-16 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='profissional',
            new_name='professor',
        ),
    ]
