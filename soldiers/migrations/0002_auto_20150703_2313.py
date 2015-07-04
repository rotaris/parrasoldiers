# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soldiers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='date_of_embarkation',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
