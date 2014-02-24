from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=(
            'django_plim',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            },
        },
        TEMPLATE_LOADERS=(
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
        ROOT_URLCONF='tests.urls',
        STATIC_URL='/static/',
        LOGGING={
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                },
            },
            'loggers': {
                '': {
                    'handler': ['console'],
                    'level': 'DEBUG',
                },
            },
        },
    )


def run():
    import sys
    from django.test.utils import get_runner

    runner = get_runner(settings)()
    failures = runner.run_tests(('django_plim',))
    sys.exit(failures)
