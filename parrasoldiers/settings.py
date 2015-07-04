"""
Django settings for parrasoldiers project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'am7rpbo!=y7pt#ulz^b&brz6s3%klwsxc()k0b2075%v)h!-wq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'soldiers',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'parrasoldiers.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'parrasoldiers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'parrasoldiers',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Custom additions (by Arun)
import os
# The list of unique_ids that don't have associated photos
LIST_OF_MISSING_SOLDIER_PHOTOS = [1, 2, 3, 4, 5, 1625, 1687, 9994, 9995, 9996, 9997, 9998, 9999, 1818, 1819, 1820, 1821, 1822, 1827, 1828, 1830, 1832, 1833, 1834, 1835, 1836, 1837, 1840, 1841, 1842, 1848, 1850, 1851, 1852, 1854, 1855, 1856, 1857, 1858, 1859, 1864, 1865, 1867, 1868, 1870, 1871, 1874, 1879, 1881, 1883, 1884, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 359, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 367, 1902, 1903, 1904, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1405, 1917, 1919, 1920, 1921, 1922, 1918, 1923, 1924, 1926, 1930, 1933, 1935, 1939, 1943, 1944, 1946, 1947, 1948, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 479]


DEFAULT_FILE_STORAGE = 'libs.storages.S3Storage.S3Storage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "NO_ACCESS_KEY_SET_IN_ENV")
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "NO_SECRET_KEY_SET_IN_ENV")
AWS_STORAGE_BUCKET_NAME = 'parrasoldiers'
