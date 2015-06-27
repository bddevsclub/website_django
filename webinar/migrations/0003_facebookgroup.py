# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinar', '0002_webinar_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('url', models.URLField(verbose_name='URL')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
