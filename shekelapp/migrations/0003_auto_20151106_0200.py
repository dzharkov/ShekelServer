# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shekelapp', '0002_auto_20151016_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(related_name='shekel', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='consumers',
            field=models.ManyToManyField(related_name='consumed_by', to='shekelapp.MyUser'),
        ),
        migrations.AlterField(
            model_name='item',
            name='customer',
            field=models.ForeignKey(related_name='bought_by', to='shekelapp.MyUser'),
        ),
    ]
