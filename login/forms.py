from django import forms
from professors.models import Professors, Appointment
from django.forms.fields import ChoiceField
from django.core.exceptions import ValidationError
STANDING = [
            ('UNDERGRADUATE','Undergraduate'),
            ('GRADUATE', 'Graduate')
            ]

class AdvisingForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 100)
    standing = forms.ChoiceField(choices = STANDING)
    advisor = forms.ModelChoiceField(queryset=Professors.objects.all())
    def clean_advisor(self):
        advisor = self.cleaned_data['advisor']
        standing = self.cleaned_data['standing']
        if (standing == 'GRADUATE') and (advisor.isGraduateAdvisor is False):
            raise ValidationError("Please select graduate advisor, Mohsen Beheshti or Jianchao Han")
        return advisor 

class DatesForm(forms.Form):
    date = forms.ModelChoiceField(queryset=Appointment.objects.all())


class EnterEmail(forms.Form):
    student_email = forms.EmailField(max_length = 100, label = 'Toro Mail')
    def clean_student_email(self):
        student_email = self.cleaned_data['student_email']
        if not student_email.endswith('toromail.csudh.edu'):
            raise ValidationError("Please enter your school email that ends with @toromail.csudh.edu")
        return student_email

class EnterCode(forms.Form):
    code = forms.CharField(max_length = 50)
