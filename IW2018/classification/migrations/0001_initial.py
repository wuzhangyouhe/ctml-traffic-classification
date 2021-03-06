# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='importData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_data', models.CharField(max_length=100)),
                ('url_target', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'importData',
                'verbose_name_plural': 'dataURL',
            },
        ),
        migrations.CreateModel(
            name='trainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature0', models.CharField(max_length=50)),
                ('feature1', models.CharField(max_length=50)),
                ('feature2', models.CharField(max_length=50)),
                ('feature3', models.CharField(max_length=50)),
                ('feature4', models.CharField(max_length=50)),
                ('feature5', models.CharField(max_length=50)),
                ('feature6', models.CharField(max_length=50)),
                ('feature7', models.CharField(max_length=50)),
                ('feature8', models.CharField(max_length=50)),
                ('feature9', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'trainData',
                'verbose_name_plural': 'dataFeatures',
            },
        ),
    ]
