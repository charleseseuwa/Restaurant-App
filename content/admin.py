from django.contrib import admin
from .models import Contact, Subscriber, Service, Menu, Booking

admin.site.register([Subscriber, Service, Menu, Booking])
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", 'email', "subject", "message"]

admin.site.register(Contact, ContactAdmin)