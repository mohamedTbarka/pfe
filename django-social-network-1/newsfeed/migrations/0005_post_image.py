# Generated by Django 3.0.2 on 2020-01-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0004_auto_20190902_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='avatars/guest.png', upload_to='posts_images'),
        ),
    ]
