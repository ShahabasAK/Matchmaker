# Generated by Django 4.1.7 on 2023-05-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datingapp', '0007_rename_request_request_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_users',
            name='status',
            field=models.CharField(default='No', max_length=20),
        ),
    ]