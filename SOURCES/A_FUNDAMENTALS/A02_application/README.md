MODULE - DJANGO APP
=======================================================================

> **Purpose**
> - creating an app
> - registering an app
> - views and routes in our app

> **Abstract**
> this section describes a basic django app creation.
> an app is formally a module containing models, views and templates.
> an app is a group of related features in a project.
> we can have multiple instances of an app per project thanks to namespaces.



<br>
***********************************************************************
<div style="page-break-after: always;"><br></div>



I - CREATE A DJANGO APP
-----------------------------------------------------------------------


###  1.1 - CREATION

```shell
django-admin startapp myapp
```


###  1.2 - STRUCTURE

```text
(django) yoyo@ICORE:A02_application$ tree --dirsfirst
.
├── myapp
│   ├── migrations
│   │   └── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── myproject
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```




###  1.3 - RUNNING

```shell
#: ./manage.py runserver 127.0.0.1:8888


Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s).
Your project may not work properly until you apply the migrations
for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 16, 2023 - 06:26:19
Django version 4.1.4, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8888/
Quit the server with CONTROL-C.

```

<br>
***********************************************************************
<div style="page-break-after: always;"><br></div>



II - REGISTER A DJANGO APP
-----------------------------------------------------------------------



###  2.1 - REGISTER APPLICATION

```python
# myproject/settings.py

INSTALLED_APPS = [
    ## add line :
    'myapp.apps.MyAppConfig'
]
```

Once our first application is registered,
Django no longer displays its default page at "/" url,
we get a normal 404 error unless we explicitely add route to /



###  2.2 - SET A URL FOR SITE ROOT

```python
## myproject/urls.py
from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse

urlpatterns = [
    path("", lambda req: HttpResponse("Welcome") ),
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls') ),
]
```



<br>
***********************************************************************
<div style="page-break-after: always;"><br></div>


**END**
