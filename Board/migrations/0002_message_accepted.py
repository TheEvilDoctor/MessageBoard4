# Generated by Django 4.1.5 on 2023-01-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
