# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRONION', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('e_mail', models.EmailField(max_length=254)),
                ('ip_address', models.GenericIPAddressField()),
                ('sub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name_plural': 'Подписчики',
                'ordering': ('name',),
                'verbose_name': 'Подписчик',
            },
        ),
    ]
