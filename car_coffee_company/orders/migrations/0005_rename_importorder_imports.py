# Generated by Django 5.0.6 on 2024-06-18 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_importorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='importOrder',
            new_name='imports',
        ),
    ]
