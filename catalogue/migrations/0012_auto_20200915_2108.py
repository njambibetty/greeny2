# Generated by Django 3.1 on 2020-09-15 18:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20200915_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=datetime.datetime(2020, 9, 15, 18, 8, 30, 613744, tzinfo=utc), upload_to='images/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
