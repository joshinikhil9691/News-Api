# Generated by Django 3.1.4 on 2020-12-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=25)),
                ('author', models.CharField(max_length=100)),
                ('article', models.CharField(max_length=1000)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]