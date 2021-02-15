from django.conf import settings

settings.configure(DEBUG=True, ROOT_URLCONF='my_app.urls')
print('good')
