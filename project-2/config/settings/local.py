from .base import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

DEBUG = True
ALLOWED_HOSTS = []

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR / 'media')


