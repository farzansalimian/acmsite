# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0002_auto_20171109_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]