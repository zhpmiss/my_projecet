# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_article_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='详细'),
        ),
    ]
