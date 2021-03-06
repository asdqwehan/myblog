#!/usr/bin/env python
# coding: utf-8

import os
import sys
import django
django.setup()

# 将系统的编码设置为UTF8
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")#mysite替换为自己的项目名

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
