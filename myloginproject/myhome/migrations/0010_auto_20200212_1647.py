# Generated by Django 3.0.2 on 2020-02-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0009_auto_20200212_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
