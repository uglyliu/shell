# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 14:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_article_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('url', models.URLField(unique=True)),
                ('description', models.CharField(default='此用户没有添加任何描述', max_length=255)),
                ('add_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]