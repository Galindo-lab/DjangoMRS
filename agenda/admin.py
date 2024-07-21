from django.contrib import admin

from .models import Contact, Event, Agenda


class ContactInline(admin.TabularInline):
    model = Agenda.contacts.through
    extra = 0


class EventInline(admin.TabularInline):
    model = Agenda.events.through
    extra = 0


class EventContactInline(admin.TabularInline):
    model = Event.contacts.through
    extra = 0


class AgendaAdmin(admin.ModelAdmin):
    inlines = [ContactInline, EventInline]
    exclude = ('notes', 'contacts', 'events')


class EventAdmin(admin.ModelAdmin):
    inlines = [EventContactInline]
    exclude = ('contacts',)


admin.site.register(Contact)
admin.site.register(Event, EventAdmin)
admin.site.register(Agenda, AgendaAdmin)
