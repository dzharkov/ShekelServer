# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shekelapp', '0005_auto_20151113_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='receipt',
        ),
        migrations.AddField(
            model_name='receipt',
            name='items',
            field=models.ManyToManyField(to='shekelapp.Item'),
        ),
    ]
