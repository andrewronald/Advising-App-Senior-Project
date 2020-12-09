## Advising-App-Senior-Project
#Created by Andrew Aguilar and Kamron Seeram
 This application is a web based advising scheduler.  Students are verified via their Toro-mail email accounts, and then given access to a form where they can view available advising dates for their desired advisor.  After they have selected their desired time and desired advisor both the student and the advisor are emailed details of the appointment.  The website is optimized to run on mobile devices as well as laptop and desktop computers. 



# Setup
1. Clone the repository:
```sh
$ git clone https://github.com/andrewronald/Advising-App-Senior-Project.git
```

2. Create a virtual environment to install requirements and activate it:
```sh
$ python3 -m venv env
$ source env/bin/activate
```

3. Now install the requirements: 
```sh
$ pip install -r requirements.txt
```

4. Once requirements are finished installing:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```

5. Finally, in a browser, navigate to http://127.0.0.1:8000/
