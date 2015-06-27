# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinar', '0003_facebookgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='embed_code',
            field=models.TextField(verbose_name='Video Embed Code', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webinar',
            name='date_time',
            field=models.DateTimeField(verbose_name='Date & Time'),
        ),
    ]
