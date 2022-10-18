# Generated by Django 4.1.2 on 2022-10-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='profile')),
                ('contact_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(default='', max_length=254)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]