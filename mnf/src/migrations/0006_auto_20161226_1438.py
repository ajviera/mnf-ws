# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20161226_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price_unit',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='price_unit',
        ),
    ]
