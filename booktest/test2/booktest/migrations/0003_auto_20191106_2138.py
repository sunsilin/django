# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20191031_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('atitle', models.CharField(max_length=30)),
                ('aParent', models.ForeignKey(to='booktest.AreaInfo', null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
