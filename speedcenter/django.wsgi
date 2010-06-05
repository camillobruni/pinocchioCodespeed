import os
import sys
sys.path.append('/home/pinocchio/codespeed')
sys.path.append('/home/pinocchio/codespeed/speedcenter/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'speedcenter.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
