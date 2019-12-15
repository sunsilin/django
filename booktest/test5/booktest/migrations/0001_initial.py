# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [

        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('goods_pic', models.ImageField(upload_to='booktest')),
            ],
        ),
    ]
