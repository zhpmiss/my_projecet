# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_article_describe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='describe',
            field=models.CharField(default='描述', max_length=300, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]