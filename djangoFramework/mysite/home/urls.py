from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "CS-ChaiWala Admin"
admin.site.site_title = "CS-ChaiWala Admin Portal"
admin.site.index_title = "Welcome to CS-ChaiWala Researcher Portal"

urlpatterns = [
    path("", views.index, name='home'),
    path("services", views.services, name='services'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
]
