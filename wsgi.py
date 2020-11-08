#!/usr/bin/env python3
import sys
import site

site.addsitedir('/var/www/money/env/lib/python3.7/site-packages')

sys.path.insert(0, '/var/www/money')

from app import app as application
