# Generated by Django 3.1.5 on 2021-01-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=True, max_length=100, null=True),
        ),
    ]