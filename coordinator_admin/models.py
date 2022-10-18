from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.
class inspector_master(models.Model):
    insp_master_full_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile')
    contact_number = models.CharField(max_length=10)
    email_id = models.EmailField(default="")
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user_name

class client_master(models.Model):
    sl_no = models.IntegerField()
    client_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name


class job_master(models.Model):
    client_name = models.ForeignKey(client_master, on_delete=models.CASCADE, related_name='c_name')
    location = models.ForeignKey(client_master, on_delete=models.CASCADE, related_name='c_location')
    date_time = models.DateTimeField('Date and Time')
    insp_master_full_name = models.ForeignKey(inspector_master, on_delete=models.CASCADE, related_name='insp_master')


    def __str__(self):
        return str(self.client_name)
