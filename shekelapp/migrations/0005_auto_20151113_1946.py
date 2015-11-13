# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shekelapp', '0004_auto_20151106_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('owner', models.ForeignKey(to='shekelapp.MyUser')),
                ('shared', models.ManyToManyField(to='shekelapp.MyUser', related_name='q')),
            ],
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='items',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='shared',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
        migrations.AddField(
            model_name='item',
            name='receipt',
            field=models.ForeignKey(default=0, to='shekelapp.Receipt', related_name='bought_in'),
            preserve_default=False,
        ),
    ]
