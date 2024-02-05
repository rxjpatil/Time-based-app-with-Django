from django.shortcuts import render
from datetime import datetime

def get_greeting(request):
    current_time = datetime.now().time()

    if current_time < datetime.strptime('06:00:00', '%H:%M:%S').time():
        greeting = 'Good Night'
    elif current_time < datetime.strptime('12:00:00', '%H:%M:%S').time():
        greeting = 'Good Morning'
    elif current_time < datetime.strptime('18:45:00', '%H:%M:%S').time():
        greeting = 'Good Afternoon'
    else:
        greeting = 'Good Evening'
    context={}
    context['greeting']=greeting

    return render(request, 'index.html',context)
