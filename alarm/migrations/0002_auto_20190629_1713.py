# Generated by Django 2.2.2 on 2019-06-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='id',
            new_name='s_id',
        ),
        migrations.RemoveField(
            model_name='spec',
            name='tof',
        ),
        migrations.RemoveField(
            model_name='spec',
            name='when',
        ),
        migrations.AlterField(
            model_name='spec',
            name='gpa',
            field=models.FloatField(max_length=50),
        ),
    ]
