from django.urls import path
from . import views
urlpatterns = [
    path('', views.login),
    path('super_admin_panel',views.super_admin_panel,name='super_admin_panel'),
    path('manager', views.fn_manager, name='manager'),
    path('coordinator', views.fn_coordinator, name='coordinator'),
    path('inspectors', views.fn_inspectors, name='inspectors'),
    path('logout',views.logout,name='logout'),

]