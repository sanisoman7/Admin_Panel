# Generated by Django 4.1.2 on 2022-10-15 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_job_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.client_master')),
            ],
        ),
    ]
