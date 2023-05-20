MODULE - DJANGO APP
=======================================================================

> **Purpose**
> - views and routes in our app


> **Abstract**
> this section describes a basic django project.
> no application will be yet created


<br>
***********************************************************************
<div style="page-break-after: always;"><br></div>


I - VIEWS AND ROUTES
-----------------------------------------------------------------------


### 1.1 VIEW

a view is a callable :
- taking at least an `HttpRequest` object as argument
- returning an `HttpResponse` object


###### A CALLABLE

- lambda
- function
- class extending `django.views.generic.View`

###### THE RESPONSE

- direct instanciation of `HttpResponse`
- rendering of a template
- raising an HttpError : 404 , 500 ...


### 1.2 ROUTE

a route is an entry in project `url_patterns` liste
routes can be : named, prefixed, part of a namespace

the django URLResolver :
will map a URL from the incomming HttpRequest,
to the corresponding view in the routes table.



###### THE DYNAMIC SEGMENTS

a route can therefor include parameters ( dynamic segments).
these dynamic segments can be expressed :
- with regular expression
- with Path converters ( django 2+ )

Custom Path converter can be created :
- a class
- having a regex field
- a to_python returning a Python type
- a to_url returning a string



### 1.3 ROUTES AND VIEWS EXEMPLES


```python
##

```

```python
##

```



<br>
***********************************************************************
<div style="page-break-after: always;"><br></div>



II - INCLUDING ROUTES IN THE PROJECTS
-----------------------------------------------------------------------


###  1.1 - URL FILE

in our app, we create a `urls.py`file
we then declare our routes into it with o liste called `url_patterns`
these will be application routes



###  1.2 - INCLUDE

```text
├── myapp
│   ├── migrations
│   │   └── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py     # <= file added
│   └── views.py
├── myproject
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py    # <= file edited
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
