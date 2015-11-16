# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shekelapp', '0006_auto_20151113_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='items',
            field=models.ManyToManyField(related_name='contains', to='shekelapp.Item'),
        ),
    ]
