# Generated by Django 2.1.2 on 2018-10-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0011_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
