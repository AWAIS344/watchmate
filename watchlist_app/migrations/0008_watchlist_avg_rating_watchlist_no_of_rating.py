# Generated by Django 5.1.6 on 2025-02-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_reviews_review_user_alter_reviews_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='no_of_rating',
            field=models.IntegerField(default=0),
        ),
    ]
