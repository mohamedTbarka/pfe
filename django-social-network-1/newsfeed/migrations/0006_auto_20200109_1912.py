# Generated by Django 3.0.2 on 2020-01-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/avatars/guest.png', upload_to='posts_images'),
        ),
    ]
