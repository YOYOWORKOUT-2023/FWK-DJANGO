DJANGO DEMOS APPLICATIONS
=======================================================================

> **Purpose**
> demo applications with for *Django framework*
> see : https://www.djangoproject.com/


> **Topics covered in demos**
> - concepts
>   - [x] project, app
>   - [x] routes, views, templates
>   - static files
>   - testing
> - crud operations
>   - models, relations, migration
>   - forms, views, templates, validation
>   - django admin
> - web features
>   - authentication, authorization
>   - sessions, cookies,
>   - caching, static files,
>   - mime files upload and generation
> - rest features
>   - expose API
>   - consume API


> **Content of this document**
> - How to run demos
> - This project directory structure
> - How to deploy
> - How to scaffold a new project
> - How to run in dev mode a new project



***********************************************************************
<div style="page-break-after: always;"></div>




I - SETUP AND RUN
-----------------------------------------------------------------------

> - install python
> - create virtual env
> - run app in virtual env


### 1.1 - Requirements

Python runtime :
- python (3.9+)
- python3-venv
- python3-pip

Python packages :
- django (3.2+)
- djangorestframework
- django-debug-toolbar


###### How to install : Ubuntu

a) Install python

```sh
sudo apt install python3-all python3-venv python3-pip
sudo apt install python-is-python3
```

b) Create virtual environment named "django"


```sh
mkdir ~/.venvs
cd ~/.venvs
python -m venv django --copies
```

Reference : doc python
https://docs.python.org/3/library/venv.html#creating-virtual-environments



###### How to install dependencies

Dependencies are located in directory : **DEPLOYKITS/requirements**

a) activate virtual environment

```sh
➜ source ~/.venv/django/bin/activate
(django) ➜  ~
```

b) install rdependencies

```sh
(django) ➜  ~ pip install -r DEPLOYMENT/requirements/dev.txt
```


### 1.2 - Run the app

for each demo, go into root folder ( eg : **SOURCE/demoxxx/**)

```sh

(django) ➜  ~ ./manage.py run server
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 01, 2022 - 08:03:40
Django version 4.0.4, using settings 'app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```




***********************************************************************
<div style="page-break-after: always;"></div>



II - REUSABLE DIRECTORY STRUCTURE
-----------------------------------------------------------------------

> The main level of directory tree contains following entries :
>
> - **APPWIKI**     : documentation for code
> - **CODEKITS**    : templates for coding
> - **DEPLOYKITS**  : templates for deploying
> - **SOURCES**     : project sources , each demo is a django project
>
> The entrypoint of the project is in `SOURCES/<demoxxx>/app/boot`
(asgi or wsgi).



### 2.1 - CODEKITS

this directory aims to contain resusable code templates.
a template could be :
- **files** for : models, views, urls, signals, middleware ...
- **folders** for : django "app"


###### commands

**scripts** : delete pythojn cache files, git commits ...
**playbooks** : github/gitlab CI workflows


###### scaffolding

django code templates

- **files** : html , views, models, templates , migrations
- **apps** : django app skeleton
  - default ( equivalent of `django-admin startapp` output )
  - custom ( used in this application, complete skeleton, see below )


###### snippets

small pieces of code, one per file ( eg: file upload, ... )

- owners : code snippets for this development
- others : code snippets grabbed from the internet


###### tools

templates for external tools (e.g. testing : coveragerc, tox.ini ...)



### 2.2 - DEPLOYKITS

deployments scripts by targets, which could be:
    - **systems** : linux, macOS ...
    - **containers** : docker, LXD, ...

python dependencies ( requirements ) by environments, which could be:
    - **DEVL** : development
    - **TEST** : testing
    - **STAG** : staging
    - **PROD** : production


###### Docker

directory for deployment on docker containers.

- Dockerfile
- Compose file
- configurations to copy in container


###### Linux

directory for deployment on linux server
scripts hat should be copied in deployment target.

**example :**

- /srv/webapps/<app_name>
- /home/gunicorn/webapps/<app_name>

**requirements on system :**

- apache + mod_wsgi ( or mod_proxy with ASGI project )
- nginx + uwsgi ( or gunicorn )


###### Requirements

various pip install requirements by environment :

- development   DEVL
- testing       TEST
- staging       STAG
- production    PROD

**Main requirement files**

- requirements.base.txt : always needed
- requirements.prod.txt : base requirements + prod specific libraries
- requirements.dev.txt : base requirements + dev specific libraries

**Example of specific requirements**

- *django-debug-toolbar* in development mode.
- *psycopg2-binary* for postgres access in production mode.



***********************************************************************
<div style="page-break-after: always;"></div>



III - SOURCES DEPLOYMENT EXAMPLE
-----------------------------------------------------------------------

> directory for django project.
> should be placed in server filesystem, example :
> - /srv/webapps/<app_name>/sources
> - /home/gunicorn/webapps/<app_name>/sources

On Linux systems:
- backend WSGI : we can deploy using `gunicorn` ( or uwsgi ) as a wsgi backend.
- front web server: we can use `nginx` for the HTTP server.
- services : for starting the services, we can use systemd.


### 3.1 - Structure of sources

***Django project***

- ***app*** : project wide code files
    - entrypoint : wsgi/asgi
    - settings
    - static
    - urls
    - views

- ***apps***        : apps folders
    - appcore       : models, views, templates
    - appaccounts   : users, groups , roles
    - appadmin      : admin website
    - appshared     : transversal utilities

- ***assets***      : optional developpment static files

- ***dbfiles***     : databases related files
    - backups       : databases backups (raw/sql exports)
    - database      : sqlite database
    - fixtures      : json files for django imports
    - rawdata       : others blobs

- ***locale***      : django translations files

- ***mediafiles***  : django temporary uploads dropspot

- ***staticfiles*** : django target directory for collectstatic

- ***templates***   : main project temmplates, overriden templates
    - app/layout    : project web page struture and components
    - app/errors    : project web page for server-side HTTP errors

- ***vendor***      : third-party dependencies ( not added with pip )
    - apps          : django apps
    - libs          : pure python libraries


###### Notes on static assets

when django `./manage.py collectstatic` is run ,
static assets are put in `staticfiles`directory.
this directory should be exposed on production webserver,
under `/static` root.



### 3.2 - Optional directories

- `demos`           :  examples of project modules

the `demos` folder is a directory safely removable.
it is used for demo/training purpose.
to run with demos mode execute `./app-rundemo.py`





***********************************************************************
<div style="page-break-after: always;"></div>



IV - PROJECT CREATION
-----------------------------------------------------------------------


### 4.1 - Prerequisites

Assuming following prerequisites are fulfilled :

- python installed
- django virtual environment created and active

```
(django) PROJECT:
```


### 4.2 - Project

```
mkdir SOURCES
cd SOURCES

django-admin startproject app .

mkdir apps demos
mkdir demos/basicdemo

django-admin startapp basicdemo demos/basicdemo
```


###### Generated project structure :

 - app
    - asgy.py               => bootstrap for ASGI servers
    - wsgi.py               => bootstrap for WSGI servers
    - urls.py               => routes
    - settings.py           => configuration
 - apps                     ( will be out project modules root )
 - demos
    - basicdemo             ( a module for demo purpose )
        - admin.py          => for django 's admin site
        - models.py         => for our models in the basicdemo module
        - tests.py          => for test cases
        - views.py          => for our views in the basicdemo module
        - apps.py           => config of basicdemo module



###### Note on namespaces for modules

Django project's module are referred as "Django application".
see : https://docs.djangoproject.com/en/dev/ref/applications/

to create applications in specific subdirectory of project,
( here we use **apps** and **demos** ),
the directory must already exists to use the namespace.
( here we created an application labeled *basicdemo* ).

and extra step is required : modify the `apps.XxxAppConfig`.

```python
# <sources_dir>/demos/basicdemo/apps.py

from django.apps import AppConfig

class BasicdemoConfig(AppConfig):
    default_auto_field  = 'django.db.models.BigAutoField'
    name                = 'demos.basicdemo'     # this is OK
    ## name = 'basicdemo'                       # this won't work

```


### 4.3 - Example of application module general structure

```text
<SOURCES>
...
apps

    module_root

        __init__.py     => python package file
        apps.py         => configuration of app

        admin/          => expose module to admin site
        api/            => expose module with restframework
        fixtures/       => module data import/export in DB
        forms/          => classes for user inputs
        management/     => commands using django management
        migrations/     => database migrations scripts
        models/         => models classes
        signals/        => events for lifecycle
        static/         => module assets
        taglibs/        => module custom tags ( templatetags )
        templates/      => module custom templates
        tests/          => unit tests for module
        urls/           => relative routes for module
        views/          => controllers for module

```


V - PROJECT EXECUTION
-----------------------------------------------------------------------


> We can locally execute project, this involves following steps :
> - activate virtual environment with dependencies installed
> - make migrations / migrate
> - define `DJANGO_SETTINGS_MODULE` in shell environment
> - run django embedded development server



### 5.1 - Makemigrations

by default, if no models are created, django applies 18 migrations.
thoses are included by django contrib modules ( auth, session, ... )

```sh
(django) YOYO SOURCES : ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

### 5.2 - runserver

```sh
(django) YOYO SOURCES : export DJANGO_SETTINGS_MODULE=app.settings.dev
(django) YOYO SOURCES : ./manage.py runserver 8888
```

###### Specific settings

Development settings and demo settings can be passed to the command.

reference : https://docs.djangoproject.com/en/dev/ref/django-admin/

```shell
./manage.py runserver  \
            127.0.0.1:8888  \
            --settings app.settings.dev
```


###### Easing scripts

Optionally , we can use easing scripts for running into specific ENV :

- **./app-rundev.py**
- **./app-rundemo.py**





***********************************************************************
<div style="page-break-after: always;"></div>


> We covered project's main directory structure in this document.
> We went into sources organization.
> We also have a bunch of reusable codes.
> Finally, we target execution environments with specific settings.



