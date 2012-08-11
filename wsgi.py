# encoding=utf-8
__author__ = 'Administrator'

import os
import sys

path = "/var/www/yeekaa"
if path not in sys.path:
    sys.path.append(path)

ppath = "/var/www"
if ppath not in sys.path:
    sys.path.append(ppath)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yeekaa.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
