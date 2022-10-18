# Generated by Django 4.1.2 on 2022-10-17 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField()),
                ('client_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='inspector_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insp_master_full_name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='profile')),
                ('contact_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(default='', max_length=254)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='job_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='Date and Time')),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_name', to='coordinator_admin.client_master')),
                ('insp_master_full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insp_master', to='coordinator_admin.inspector_master')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_location', to='coordinator_admin.client_master')),
            ],
        ),
    ]