# Generated by Django 2.2 on 2020-02-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_flatpages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='template_name',
            field=models.CharField(blank=True, choices=[('default_decouvrir.html', 'flatpages/default_decouvrir.html'), ('default.html', 'flatpages/default.html')], help_text="Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'.", max_length=70, verbose_name='templates name'),
        ),
    ]