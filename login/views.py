from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string
from .forms import AdvisingForm, EnterEmail, EnterCode, DatesForm
from professors.models import Professors, Appointment
from django.core.mail import send_mail
import secrets
def login(request):
    if request.method == 'POST':
        form = EnterEmail(request.POST)
        if form.is_valid():
            student_email = form.cleaned_data['student_email']
            token = secrets.token_urlsafe(20)
            subject = "Please enter the code to login"
            message = f'Please enter the code here: {token}'
            send_mail(subject, message, 'advising.csc.csudh@gmail.com', [student_email])
            request.session['token'] = token
            request.session['student_email'] = student_email
            return HttpResponseRedirect('/enter_code/')
    else:
        form = EnterEmail()
    return render(request, 'login/login.html', {'form' : form})
def home(request):
    return render(request, 'login/home.html')
def emailCode(request):
    token = request.session.get('token')
    if request.method == 'POST':
        form = EnterCode(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if token == code:
                try:
                    print("test")#del request.session['token']
                except KeyError:
                    pass
                return HttpResponseRedirect('/advising_form/')
    else:
        form = EnterCode()
    return render(request, 'login/enter_code.html', {'form' : form})

def available_appointments(request):
    advisor = request.session.get('selected_advisor')
    advisor_name = request.session.get('advisor_name')
    student_name = request.session.get('student_name')
    advisor_email = request.session.get('advisor_email')
    student_email = request.session.get('student_email')
    appointments = Appointment.objects.filter(advisor_id = advisor)
    print(appointments)
    if request.method == 'POST':
        if request.session.get('token') is None:
            return HttpResponseRedirect('/login/')
        form = DatesForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            subject = "Appointment Confirmed"
            message_advisor= f'An appointment has been confirmed! \nDate: {date} \nStudent : {student_name}'
            message_student = f'Your appointment has been confirmed! \n Date: {date} \n Advisor : {advisor_name}'
            send_mail(subject, message_advisor, 'advising.csc.csudh@gmail.com', [advisor_email])
            send_mail(subject, message_student, 'advising.csc.csudh@gmail.com', [student_email])
            Appointment.objects.filter(id=date.id).delete()
            return HttpResponseRedirect('/confirmed/')
    else:
        if request.session.get('token') is None:
            return HttpResponseRedirect('/login/')
        form = DatesForm()
        form.fields['date'].queryset = Appointment.objects.filter(advisor_id = advisor)
    return render(request, 'login/available_appointments.html', {'form' : form, 'advisor_name' : advisor_name})


def confirmed(request):
    try:
        del request.session['token']
    except KeyError:
        pass
    return render(request, 'login/confirmed.html')

def advisingForm(request):
    student_email=request.session.get('student_email')
    if request.method == 'POST':
        form = AdvisingForm(request.POST)
        if form.is_valid():
            #date = form.cleaned_data['date']
            advisor = form.cleaned_data['advisor']
            request.session['advisor_name'] = advisor.first_name + " " + advisor.last_name
            request.session['advisor_email'] = advisor.professor_email
            #selected_advisor = advisor
            student_name = form.cleaned_data['first_name'] +" "+ form.cleaned_data['last_name']
            request.session['student_name'] = student_name
            #student_email = form.cleaned_data['student_email']
            request.session['selected_advisor'] = advisor.id
            return HttpResponseRedirect('/available_appointments/')

    else:
        if request.session.get('token') is None:
            return HttpResponseRedirect('/login/')
        form = AdvisingForm()
    return render(request, 'login/advising_form.html', {'form' : form})
