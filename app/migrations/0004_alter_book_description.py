# Generated by Django 4.2.3 on 2023-07-24 16:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_quote_author_quote_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]