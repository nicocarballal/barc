# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('data_api', '0011_auto_20150627_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinaryBlob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.CharField(max_length=128, db_index=True)),
                ('name', models.CharField(max_length=128, db_index=True)),
                ('group', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='setting',
            name='group',
            field=models.ManyToManyField(to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='program',
            name='sleep_time_sec',
            field=models.FloatField(default=1.0),
        ),
    ]
