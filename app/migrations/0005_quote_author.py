# Generated by Django 4.2.3 on 2023-10-06 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_quote_meta_description_quote_meta_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
    ]
