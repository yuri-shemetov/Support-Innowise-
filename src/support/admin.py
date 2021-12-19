from django.contrib import admin
from .models import Status, Ticket, Contact

class TicketAdmin(admin.ModelAdmin):
    list_display=['author', 'created', 'title', 'text', 'status']

class ContactAdmin(admin.ModelAdmin):
    list_display=['name', 'email']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Status)
admin.site.register(Contact, ContactAdmin)