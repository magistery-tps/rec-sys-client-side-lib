# Generated by Django 4.1 on 2022-12-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recsysweb', '0026_recommender_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommender',
            name='enable',
            field=models.BooleanField(default=True, verbose_name='Enable/Disable Recommender'),
        ),
    ]
