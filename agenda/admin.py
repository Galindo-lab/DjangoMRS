from django.contrib import admin
from .models import Agenda, Contact, Event


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class EventInline(admin.StackedInline):
    model = Event
    extra = 0


class AgendaAdmin(admin.ModelAdmin):
    inlines = [ContactInline, EventInline]
    list_display = ('user',)
    search_fields = ('user__username',)
    list_filter = ('user',)


class EventContactInline(admin.TabularInline):
    model = Event.contacts.through
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [EventContactInline]
    list_display = ('title', 'start_time', 'end_time', 'agenda')
    search_fields = ('title',)
    list_filter = ('start_time', 'end_time', 'agenda')


admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Contact)
admin.site.register(Event, EventAdmin)
