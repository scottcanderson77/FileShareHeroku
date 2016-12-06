# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicKey', models.CharField(max_length=1024)),
                ('privateKey', models.CharField(default=1, max_length=1024)),
                ('sentMessagesScene', models.IntegerField(default=0)),
                ('recMessagesScene', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]