from django.contrib import admin
from .models import Status, Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display=['author', 'created', 'title', 'text', 'status']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Status)
