import json

from django.db import models
import datetime


class Calendar(models.Model):
    """
    Represents the calendar in the agenda.

    Attributes:
        events (QuerySet[Event]): A list of events in the calendar.
    """
    events = models.ManyToManyField('Event', related_name='calendars')

    def add_event(self, event):
        """
        Adds an event to the calendar.

        :param event: The event to add.
        :type event: Event
        """
        self.events.add(event)

    def get_events(self):
        """
        Gets all events in the calendar.

        :return: A queryset of events.
        :rtype: QuerySet[Event]
        """
        return self.events.all()


class Task(models.Model):
    """
    Represents a task in the agenda.

    Attributes:
        title (str): The title of the task.
        description (str): The description of the task.
        due_date (date): The due date of the task.
        completed (bool): Whether the task is completed.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def create_task(self, title, description, due_date):
        """
        Creates a new task.

        :param title: The title of the task.
        :type title: str
        :param description: The description of the task.
        :type description: str
        :param due_date: The due date of the task.
        :type due_date: date
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.save()

    def read_task(self):
        """
        Reads the task details.

        :return: The task instance.
        :rtype: Task
        """
        return self


class Note(models.Model):
    """
    Represents a note in the agenda.

    Attributes:
        title (str): The title of the note.
        content (str): The content of the note.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()

    def create_note(self, title, content):
        """
        Creates a new note.

        :param title: The title of the note.
        :type title: str
        :param content: The content of the note.
        :type content: str
        """
        self.title = title
        self.content = content
        self.save()

    def read_note(self):
        """
        Reads the note details.

        :return: The note instance.
        :rtype: Note
        """
        return self


class Contact(models.Model):
    """
    Represents a contact in the agenda.

    Attributes:
        name (str): The name of the contact.
        phone (str): The phone number of the contact.
        email (str): The email address of the contact.
    """
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def create_contact(self, name, phone, email):
        """
        Creates a new contact.

        :param name: The name of the contact.
        :type name: str
        :param phone: The phone number of the contact.
        :type phone: str
        :param email: The email address of the contact.
        :type email: str
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.save()

    def read_contact(self):
        """
        Reads the contact details.

        :return: The contact instance.
        :rtype: Contact
        """
        return self


class Event(models.Model):
    """
    Represents an event in the calendar.

    Attributes:
        title (str): The title of the event.
        description (str): The description of the event.
        date (date): The date of the event.
        start_time (datetime): The start time of the event.
        end_time (datetime): The end time of the event.
        contacts (QuerySet[Contact]): A list of contacts involved in the event.
        reminders (QuerySet[Reminder]): A list of reminders for the event.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    contacts = models.ManyToManyField('Contact', related_name='events')
    reminders = models.ManyToManyField('Reminder', related_name='events')

    def to_dict(self):
        return {
            'name': self.title,
            'start': self.start_time,
            'end': self.end_time
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def create_event(self, title, description, date, start_time, end_time):
        """
        Creates a new event.

        :param title: The title of the event.
        :type title: str
        :param description: The description of the event.
        :type description: str
        :param date: The date of the event.
        :type date: date
        :param start_time: The start time of the event.
        :type start_time: datetime
        :param end_time: The end time of the event.
        :type end_time: datetime
        """
        self.title = title
        self.description = description
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.save()

    def read_event(self):
        """
        Reads the event details.

        :return: The event instance.
        :rtype: Event
        """
        return self


class Reminder(models.Model):
    """
    Represents a reminder for an event.

    Attributes:
        message (str): The reminder message.
        date_time (datetime): The date and time of the reminder.
    """
    message = models.CharField(max_length=255)
    date_time = models.DateTimeField()

    def create_reminder(self, message, date_time):
        """
        Creates a new reminder.

        :param message: The reminder message.
        :type message: str
        :param date_time: The date and time of the reminder.
        :type date_time: datetime
        """
        self.message = message
        self.date_time = date_time
        self.save()

    def read_reminder(self):
        """
        Reads the reminder details.

        :return: The reminder instance.
        :rtype: Reminder
        """
        return self


class Agenda(models.Model):
    """
    Represents the agenda containing all other sections.

    Methods:
        add_calendar(calendar)
        get_calendar()
        add_task(task)
        get_tasks()
        add_note(note)
        get_notes()
        add_contact(contact)
        get_contacts()
        add_event(event)
        get_events()
        add_reminder(reminder)
        get_reminders()
    """
    calendar = models.OneToOneField(Calendar, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, related_name='agendas')
    notes = models.ManyToManyField(Note, related_name='agendas')
    contacts = models.ManyToManyField(Contact, related_name='agendas')
    events = models.ManyToManyField(Event, related_name='agendas')
    reminders = models.ManyToManyField(Reminder, related_name='agendas')

    def add_calendar(self, calendar):
        """
        Adds a calendar to the agenda.

        :param calendar: The calendar to add.
        :type calendar: Calendar
        """
        self.calendar = calendar
        self.save()

    def get_calendar(self):
        """
        Gets the calendar of the agenda.

        :return: The calendar instance.
        :rtype: Calendar
        """
        return self.calendar

    def add_task(self, task):
        """
        Adds a task to the agenda.

        :param task: The task to add.
        :type task: Task
        """
        self.tasks.add(task)

    def get_tasks(self):
        """
        Gets all tasks in the agenda.

        :return: A queryset of tasks.
        :rtype: QuerySet[Task]
        """
        return self.tasks.all()

    def add_note(self, note):
        """
        Adds a note to the agenda.

        :param note: The note to add.
        :type note: Note
        """
        self.notes.add(note)

    def get_notes(self):
        """
        Gets all notes in the agenda.

        :return: A queryset of notes.
        :rtype: QuerySet[Note]
        """
        return self.notes.all()

    def add_contact(self, contact):
        """
        Adds a contact to the agenda.

        :param contact: The contact to add.
        :type contact: Contact
        """
        self.contacts.add(contact)

    def get_contacts(self):
        """
        Gets all contacts in the agenda.

        :return: A queryset of contacts.
        :rtype: QuerySet[Contact]
        """
        return self.contacts.all()

    def add_event(self, event):
        """
        Adds an event to the agenda.

        :param event: The event to add.
        :type event: Event
        """
        self.events.add(event)

    def get_events(self):
        """
        Gets all events in the agenda.

        :return: A queryset of events.
        :rtype: QuerySet[Event]
        """
        return self.events.all()

    def add_reminder(self, reminder):
        """
        Adds a reminder to the agenda.

        :param reminder: The reminder to add.
        :type reminder: Reminder
        """
        self.reminders.add(reminder)

    def get_reminders(self):
        """
        Gets all reminders in the agenda.

        :return: A queryset of reminders.
        :rtype: QuerySet[Reminder]
        """
        return self.reminders.all()
