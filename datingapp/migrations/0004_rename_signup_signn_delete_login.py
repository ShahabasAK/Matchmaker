# Generated by Django 4.1.2 on 2023-05-03 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datingapp', '0003_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='signn',
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
