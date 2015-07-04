# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soldiers', '0003_auto_20150703_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='unit_served',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
