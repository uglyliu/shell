# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
