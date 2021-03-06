# Generated by Django 2.2.2 on 2019-06-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tof', models.IntegerField(max_length=50)),
                ('gpa', models.IntegerField(max_length=50)),
                ('when', models.IntegerField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('univ_name', models.CharField(max_length=100)),
                ('kor_name', models.CharField(max_length=100)),
                ('depart', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('준비중', '준비'), ('파견완료', '완료')], default='준비중', max_length=50)),
            ],
        ),
    ]
