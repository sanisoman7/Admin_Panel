# Generated by Django 4.1.2 on 2022-10-15 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_job_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_master',
            name='c_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_location', to='home.client_master'),
        ),
        migrations.AlterField(
            model_name='job_master',
            name='client_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_name', to='home.client_master'),
        ),
    ]
