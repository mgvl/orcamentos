# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-01 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='customer_type',
            field=models.CharField(blank=True, choices=[('c', 'construtora'), ('a', 'arquitetura'), ('p', 'particular')], max_length=1, null=True, verbose_name='tipo de cliente'),
        ),
    ]