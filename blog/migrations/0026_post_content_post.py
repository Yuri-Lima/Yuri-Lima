# Generated by Django 3.1.5 on 2021-02-17 15:44

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20210216_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_post',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]