"""advising_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import professors.views
import login.views
admin.site.site_header = "CSUDH Advising Admin Page"
admin.site.index_title = "CSUDH Advising Admin Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('professors/', professors.views.index, name='professor_page'),
    path('login/', login.views.login, name='login_page'),
    path('', login.views.home, name='home'),
    path('enter_code/', login.views.emailCode, name='emailCode'),
    path('advising_form/', login.views.advisingForm, name='advisingForm'),
    path('confirmed/', login.views.confirmed, name='confirmed'),
    path('available_appointments/', login.views.available_appointments, name='available_appointments')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
