# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soldiers', '0004_auto_20150704_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='service_no',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
