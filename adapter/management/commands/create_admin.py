from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Activate a fixed locale, e.g. Russian
        translation.activate('ru')
        # Or you can activate the LANGUAGE_CODE # chosen in the settings:
        from django.conf import settings
        translation.activate(settings.LANGUAGE_CODE)
        # Your command logic here
        user_model = get_user_model()
        user_data = {
            "username": "admin",
            "password": "admin123",
            "email": "rocky@163.com"
        }
        user_model.objects.create_superuser(**user_data)
        translation.deactivate()
