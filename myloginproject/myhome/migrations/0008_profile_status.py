# Generated by Django 3.0.2 on 2020-02-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(default='active', max_length=10),
        ),
    ]
