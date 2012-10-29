# encoding=utf-8

import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'yeekaa.urls'

WSGI_APPLICATION = "yeekaa.wsgi.application"

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (os.path.join(SITE_ROOT, 'templates').replace('\\','/'),)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

STATIC_ROOT = ''  # 不要将自己的文件放在这里，这是 manage.py collectstatics 命令所收集文件放置的地方
STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'static').replace('\\', '/'),)
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

INSTALLED_APPS = (
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'debug_toolbar',
    'south',
    'yeekaa.baseinfo',
    )

MIDDLEWARE_CLASSES = (
    #'django.middleware.common.CommonMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    )

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.dirname(__file__), 'databases/yeekaa.db').replace('\\','/'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
            }
        },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
    }

SITE_ID = 1
SECRET_KEY = '0hka9l@a1vt-gg2x&_f6znygiq&vo)b_n3nm7rs1=4oifi=d@c'

INTERNAL_IPS = ('127.0.0.1',)

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'utf-8'
USE_I18N = True
USE_L10N = True

ADMINS = (('Zhao', 'zztemp001@gmail.com'),)
MANAGERS = ADMINS
ADMIN_MEDIA_PREFIX = '/statica/admin/'