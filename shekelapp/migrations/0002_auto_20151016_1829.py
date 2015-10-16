# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shekelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='consumers',
            field=models.ManyToManyField(to='shekelapp.MyUser', related_name='consumed'),
        ),
        migrations.AddField(
            model_name='item',
            name='customer',
            field=models.ForeignKey(to='shekelapp.MyUser', related_name='bought', default=1),
            preserve_default=False,
        ),
    ]
