# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=250)),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Date & Time')),
                ('video_url', models.URLField(verbose_name='Video URL')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
