# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AcessRecord',
            new_name='AccessRecord',
        ),
    ]