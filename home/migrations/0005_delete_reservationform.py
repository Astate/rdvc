# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_reservationform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReservationForm',
        ),
    ]
