# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 23:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysiteVf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogada',
            options={'ordering': ['created_date'], 'verbose_name': 'Joggada', 'verbose_name_plural': 'Jogadas'},
        ),
    ]
