# Generated by Django 3.2 on 2021-05-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitshifts', '0006_auto_20210515_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitshift',
            name='fromtime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submitshift',
            name='totime',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
