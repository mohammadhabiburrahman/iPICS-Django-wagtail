from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# CORS_ORIGIN_WHITELIST = (
#   'https://apiipics.inneedcloud.com', 'http://apiipics.inneedcloud.com'
# )


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k!vlkk#eczj+(jva*&zm39(d9drm1u=#a^@qj=h^*mdt1ynt0x'

# SECURITY WARNING: define the correct hosts in production!



# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['44.207.172.150','stgapi.inneedcloud.com','0.0.0.0','apiipics.inneedcloud.com','127.0.0.1','localhost', '3.224.227.254', 'testapi.inneedcloud.com','demoapplb-946665656.us-east-1.elb.amazonaws.com', 'localhost:8000','3.224.227.254','138.2.94.85'] 
CSRF_TRUSTED_ORIGINS = ['https://*.inneedcloud.com','https://*.127.0.0.1','https://44.207.172.150','http://44.207.172.150','http://*.inneedcloud.com','https://0.0.0.0','https://stgapi.inneedcloud.com','http://stgapi.inneedcloud.com']

# ALLOWED_HOSTS = ['44.207.172.150','0.0.0.0','stgapi.inneedcloud.com'] 
# CSRF_TRUSTED_ORIGINS = ['https://*.inneedcloud.com','https://*.127.0.0.1','https://44.207.172.150','http://44.207.172.150','https://stgapi.inneedcloud.com','http://stgapi.inneedcloud.com']


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
