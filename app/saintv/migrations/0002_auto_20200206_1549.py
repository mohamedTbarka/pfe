# Generated by Django 2.2 on 2020-02-06 15:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('saintv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='ticket',
        ),
        migrations.AddField(
            model_name='participation',
            name='hash_code',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Hash code'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Nom et prénom'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_participations', to='saintv.Response', verbose_name='Réponse'),
        ),
        migrations.AlterField(
            model_name='response',
            name='response',
            field=models.TextField(verbose_name='Réponse'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date dernière mise à jour')),
                ('ticket', models.ImageField(blank=True, null=True, upload_to='tickets')),
                ('ticket_base64', models.TextField(blank=True, editable=False, null=True)),
                ('participant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_tickets', to='saintv.Participant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='participation',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticketparticipations', to='saintv.Ticket', verbose_name='Réponse'),
        ),
    ]