# Generated by Django 3.0.2 on 2020-02-08 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0005_auto_20200208_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='projectslist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myhome.ProjectsList'),
        ),
    ]