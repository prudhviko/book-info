# Generated by Django 4.2.3 on 2023-10-06 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_quote_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
    ]
#