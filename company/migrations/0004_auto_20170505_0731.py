# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 07:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_userprofile_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='company',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]