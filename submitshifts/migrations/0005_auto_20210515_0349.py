# Generated by Django 3.2 on 2021-05-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitshifts', '0004_auto_20210514_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitshift',
            name='fromtime',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='submitshift',
            name='totime',
            field=models.TimeField(blank=True),
        ),
    ]
