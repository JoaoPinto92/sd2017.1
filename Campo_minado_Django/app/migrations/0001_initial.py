# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 01:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha', models.CharField(max_length=2)),
                ('coluna', models.CharField(max_length=2)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('adversario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adversario', to=settings.AUTH_USER_MODEL)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
