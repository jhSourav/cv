# Generated by Django 2.1.2 on 2018-10-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_auto_20181009_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('projet1', models.CharField(max_length=100)),
                ('projet2', models.CharField(max_length=100)),
                ('projet3', models.CharField(max_length=100)),
                ('projet4', models.CharField(max_length=100)),
                ('projet5', models.CharField(max_length=100)),
            ],
        ),
    ]
