# Generated by Django 3.1.7 on 2021-03-29 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bullsAndCows', '0003_auto_20210329_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='guess',
            field=models.CharField(max_length=40),
        ),
    ]
