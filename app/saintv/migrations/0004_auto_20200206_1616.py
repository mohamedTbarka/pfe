# Generated by Django 2.2 on 2020-02-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saintv', '0003_response_is_true'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='is_True',
            field=models.BooleanField(default=False, verbose_name='Vrais?'),
        ),
    ]
