# Generated by Django 2.2.6 on 2023-12-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20231228_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='indeedjobs',
            name='description',
            field=models.TextField(default='No Description'),
            preserve_default=False,
        ),
    ]
