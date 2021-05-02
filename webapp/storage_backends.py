from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class StaticFileStorge(S3Boto3Storage):
    location = settings.STATIC_LOCATION
    default_acl = "public-read"

class PublicMediaStorge(S3Boto3Storage):
    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = "public-read"
    file_overwite = False

