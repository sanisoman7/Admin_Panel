# Generated by Django 4.1.2 on 2022-10-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_job_master_c_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_master',
            name='Inspector',
            field=models.ManyToManyField(to='home.inspector'),
        ),
    ]
