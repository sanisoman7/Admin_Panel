from django.urls import path
from . import views
urlpatterns = [
    path('', views.login),
    path('coordinator', views.fun_coordinator, name='coordinator'),
    path('logout',views.logout,name='logout'),


]