# Generated by Django 3.1.5 on 2021-12-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendContactEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('from_email', models.EmailField(max_length=60, verbose_name='Email')),
                ('to_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
