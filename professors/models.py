from django.db import models
from datetime import datetime
class Professors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    isGraduateAdvisor = models.BooleanField(default = False, verbose_name='Graduate Advisor')
    profile_image = models.ImageField(upload_to='images/', default='images/default_profile_image.jpg')
    professor_text = models.TextField(default = " ", blank=True)
    professor_email = models.EmailField(default = 'advising.csc.csudh@gmail.com')
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
class Appointment(models.Model):
    advisor = models.ForeignKey(Professors, on_delete=models.CASCADE)
    time = models.DateTimeField(unique = True)
    def __str__(self):
        formatted = self.time.strftime("%a %b %d, %Y %I:%M:%p")
        #formatted = str(self.advisor)+", " + formatted
        return formatted
