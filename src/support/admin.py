from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display=['author', 'created', 'title', 'text']

admin.site.register(Ticket, TicketAdmin)
