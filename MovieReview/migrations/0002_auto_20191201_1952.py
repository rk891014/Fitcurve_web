# Generated by Django 2.2.7 on 2019-12-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='movie_genere',
            new_name='movie_type',
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='movie_detail',
            field=models.TextField(default=' ', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='movie_release_date',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
