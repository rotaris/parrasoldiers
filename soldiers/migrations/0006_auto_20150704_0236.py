# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soldiers', '0005_auto_20150704_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='unique_id',
            field=models.IntegerField(unique=True),
        ),
    ]
