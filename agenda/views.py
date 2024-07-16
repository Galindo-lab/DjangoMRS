from django.shortcuts import render


# Create your views here.
def calendarView(request):
    return render(request, 'calendar.html')
