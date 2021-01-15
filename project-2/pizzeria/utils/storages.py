from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage, SpooledTemporaryFile
import os
    

class MediaStorage(S3Boto3Storage):
    location = settings.AWS_MEDIA_LOCATION
    file_overwrite = False
    
    # http://bit.ly/2YQGz0I
    def _save(self, name, content):
        content.seek(0, os.SEEK_SET)
        with SpooledTemporaryFile() as content_autoclose:
            content_autoclose.write(content.read())
            return super(MediaStorage, self)._save(name, content_autoclose)