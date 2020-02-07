# Generated by Django 2.2 on 2020-02-07 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saintv', '0006_auto_20200206_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='participant',
            name='telephone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='participation',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticketparticipations', to='saintv.Ticket', verbose_name='Ticket'),
        ),
    ]