"""
ASGI config for sr_1_jasminSmayilova1SE project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sr_1_jasminSmayilova1SE.settings')

application = get_asgi_application()
