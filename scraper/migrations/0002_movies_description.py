# Generated by Django 4.2.6 on 2023-10-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
