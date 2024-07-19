from django.contrib import admin

from agenda.models import Activity

# Register your models here.
from django.contrib import admin
from .models import Calendar, Task, Note, Contact, Event, Reminder, Agenda

class TaskInline(admin.TabularInline):
    model = Agenda.tasks.through
    extra = 1

class NoteInline(admin.TabularInline):
    model = Agenda.notes.through
    extra = 1

class ContactInline(admin.TabularInline):
    model = Agenda.contacts.through
    extra = 1

class EventInline(admin.TabularInline):
    model = Agenda.events.through
    extra = 1

class ReminderInline(admin.TabularInline):
    model = Agenda.reminders.through
    extra = 1

class CalendarEventInline(admin.TabularInline):
    model = Calendar.events.through
    extra = 1

class EventContactInline(admin.TabularInline):
    model = Event.contacts.through
    extra = 1

class EventReminderInline(admin.TabularInline):
    model = Event.reminders.through
    extra = 1

class CalendarAdmin(admin.ModelAdmin):
    inlines = [CalendarEventInline]
    exclude = ('events',)

class AgendaAdmin(admin.ModelAdmin):
    inlines = [TaskInline, NoteInline, ContactInline, EventInline, ReminderInline]

class EventAdmin(admin.ModelAdmin):
    inlines = [EventContactInline, EventReminderInline]

admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Task)
admin.site.register(Note)
admin.site.register(Contact)
admin.site.register(Event, EventAdmin)
admin.site.register(Reminder)
admin.site.register(Agenda, AgendaAdmin)


admin.site.register(Activity)