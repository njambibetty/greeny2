# Generated by Django 3.1 on 2020-09-13 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20200913_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
    ]
