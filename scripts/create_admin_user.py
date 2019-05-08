"""An script to create the default admin user in the current Django project."""
import os
from django.contrib.auth.models import User


def run():
    if "DEFAULT_ADMIN_USER" in os.environ and "DEFAULT_ADMIN_PASSWORD" in os.environ:
        user = User.objects.create_user(
            os.environ['DEFAULT_ADMIN_USER'],
            password=os.environ['DEFAULT_ADMIN_PASSWORD']
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
