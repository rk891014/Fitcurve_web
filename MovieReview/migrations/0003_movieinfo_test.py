# Generated by Django 2.2.7 on 2019-12-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReview', '0002_auto_20191201_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo_Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_test', models.CharField(max_length=200)),
            ],
        ),
    ]