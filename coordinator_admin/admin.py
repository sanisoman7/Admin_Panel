from django.contrib import admin
import django.apps
from . models import *

# # Register your models here.
class coordinator_admin_area(admin.AdminSite):
    site_header = 'Coordinator Admin Area'
coordin_site = coordinator_admin_area(name='CoordinatorAdmin')
class clientmaster(admin.ModelAdmin):
    list_display=('sl_no', 'client_name', 'location')
coordin_site.register(client_master, clientmaster)
coordin_site.register(job_master)
coordin_site.register(inspector_master)





