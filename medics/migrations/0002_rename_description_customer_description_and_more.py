# Generated by Django 5.0 on 2024-02-03 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='price',
            new_name='Price',
        ),
    ]
