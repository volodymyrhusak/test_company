# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 22:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_userprofile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.CompanyModel'),
        ),
    ]
