# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0012_auto_20161226_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
