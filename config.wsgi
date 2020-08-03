#!/usr/bin/python
import sys
import logging
import site

# this tells wsgi where the libraries are
site.addsitedir('/var/www/flask-app/venv/lib/python3.7/site-packages')
logging.basicConfig(stream=sys.stderr)

# name of the top level folder for the project
sys.path.insert(0,"/var/www/flask-app/")

# from [[your project name]]
from app import app as application
application.secret_key = 'key'

