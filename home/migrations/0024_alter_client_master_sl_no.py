# Generated by Django 4.1.2 on 2022-10-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_job_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_master',
            name='sl_no',
            field=models.IntegerField(default=1),
        ),
    ]
