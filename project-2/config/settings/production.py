from .base import *
import dj_database_url
DEBUG = False
ALLOWED_HOSTS = ['pizzeria01.herokuapp.com']

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'pizzeria'
AWS_LOCATION = 'static'
AWS_MEDIA_LOCATION = 'media'
AWS_S3_CUSTOM_DOMAIN = 'dcj5ejzj82or5.cloudfront.net'
AWS_DEFAULT_ACL = None
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'pizzeria.utils.storages.MediaStorage'