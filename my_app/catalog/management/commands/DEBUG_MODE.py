from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        settings.DEBUG = True
        settings.ALLOWED_HOSTS[0] = 'test'
        print('all done')
        settings.ALLOWED_HOSTS[1] = 'test'
        print('all done2')
        """
        print('test')
        settings.configure(ALLOWED_HOSTS = [
            'localhost',
            '127.0.0.1',
        ],
            DEBUG=False)
        """
