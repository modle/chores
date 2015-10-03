import os
import urlparse

urlparse.uses_netloc.append("postgres")
assert 'DATABASE_URL' in os.environ, 'Set DATABASE_URL in your .env file!'
url = urlparse.urlparse(os.environ["DATABASE_URL"])

SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port
    }
}

DEBUG = os.environ["DEBUG"]
