# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 00:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('headland_app', '0002_images_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
    ]