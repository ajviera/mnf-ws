# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_auto_20161226_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='total_price',
        ),
    ]
