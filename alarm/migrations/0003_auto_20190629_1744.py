# Generated by Django 2.2.2 on 2019-06-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0002_auto_20190629_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='tof',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spec',
            name='when',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
