# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-15 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conley', '0003_auto_20161115_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='upload_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]