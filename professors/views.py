from django.shortcuts import render
from .models import Professors, Appointment
#from django.http import HttpResponse
def index(request):
    professor = Professors.objects
    appointment = Appointment.objects
    return render(request, 'professors/index.html', {'professor':professor, 'appointment':appointment})
    #return HttpResponse("Hello World!!!!. This is the Professors Page")
