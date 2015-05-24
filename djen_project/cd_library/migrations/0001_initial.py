# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('artist', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('genre', models.CharField(max_length=1, choices=[(b'R', b'Rock'), (b'B', b'Blues'), (b'J', b'Jazz'), (b'P', b'Pop')])),
            ],
        ),
    ]
