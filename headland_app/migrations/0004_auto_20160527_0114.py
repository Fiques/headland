# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 01:14
from __future__ import unicode_literals

import awesome_avatar.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headland_app', '0003_auto_20160527_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=awesome_avatar.fields.AvatarField(null=True, upload_to='avatars'),
        ),
    ]
