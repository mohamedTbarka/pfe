# Generated by Django 2.2 on 2020-02-06 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saintv', '0005_auto_20200206_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response_participations', to='saintv.Response', verbose_name='Réponse'),
        ),
    ]