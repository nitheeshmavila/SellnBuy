# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-17 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbapp', '0002_auto_20161217_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_logo',
            new_name='item_image',
        ),
    ]
