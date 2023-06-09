# Generated by Django 4.1.7 on 2023-05-22 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datingapp', '0005_signn_bio_signn_dob_signn_gender_signn_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now=True)),
                ('idreciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to='datingapp.signn')),
                ('idrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to='datingapp.signn')),
            ],
        ),
    ]
