# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('webinar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
