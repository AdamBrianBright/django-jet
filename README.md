# Django JET (Django-3 compatible)

> Fork from https://github.com/mariusionescu/django-jet

## Installation

* Download and install the Django3 compatible version of Django JET:
    - `poetry add cifrazia-django-jet`
    - `pip install cifrazia-django-jet`
    - `easy_install cifrazia-django-jet`
* Add 'jet' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be
  before 'django.contrib.admin'):

```python
INSTALLED_APPS = [
    ...,
    'jet',
    'django.contrib.admin',
]
```

* Make sure ``django.template.context_processors.request`` context processor is enabled in settings.py (Django 1.8+
  way):

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...,
                'django.template.context_processors.request',
                ...
            ],
        },
    },
]
```

* Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and
  autocompletes):

```python
urlpatterns = [
    '',
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', include(admin.site.urls)),
    ...
]
```

* Create database tables (chose):
    - `python manage.py migrate jet`
    - `python manage.py syncdb`

* Collect static if you are in production environment:
    - `python manage.py collectstatic`

* Clear your browser cache
