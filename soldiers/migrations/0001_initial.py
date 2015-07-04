# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('contributor', models.CharField(max_length=40, default='', blank=True)),
                ('unique_id', models.IntegerField()),
                ('pds_page_no', models.CharField(max_length=50, default='', blank=True)),
                ('district', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100, blank=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('rank', models.CharField(max_length=100, blank=True)),
                ('desc', models.TextField(blank=True)),
                ('unit_served', models.CharField(max_length=100, blank=True)),
                ('service_no', models.CharField(max_length=40)),
                ('date_of_embarkation', models.DateTimeField(blank=True)),
                ('died_in_service', models.CharField(max_length=40, default='', blank=True)),
            ],
        ),
    ]
