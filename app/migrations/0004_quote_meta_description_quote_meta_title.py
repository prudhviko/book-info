# Generated by Django 4.2.3 on 2023-10-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_quote_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='meta_description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='meta_title',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
