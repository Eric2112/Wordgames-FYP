# Generated by Django 3.1.7 on 2021-03-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bullsAndCows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess', models.CharField(max_length=40)),
            ],
        ),
    ]
