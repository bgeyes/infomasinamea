# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('make_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='home.Make')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('year', models.IntegerField(blank=True)),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='home.Model')),
            ],
        ),
    ]
