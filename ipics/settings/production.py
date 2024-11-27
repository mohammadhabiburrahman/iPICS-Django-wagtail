from .base import *

DEBUG = False

# CORS_ORIGIN_WHITELIST = (
#   'https://apiipics.inneedcloud.com', 'http://apiipics.inneedcloud.com'
# )


# ALLOWED_HOSTS = ['0.0.0.0','apiipics.inneedcloud.com'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("MYSQL_DB"),
        'USER': os.getenv("MYSQL_USER"),
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST': os.getenv("MYSQL_HOST"),
        'PORT': os.getenv("MYSQL_PORT"),
    }
}


# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['44.207.172.150','0.0.0.0','apiipics.inneedcloud.com','127.0.0.1','localhost', '3.224.227.254', 'testapi.inneedcloud.com','demoapplb-946665656.us-east-1.elb.amazonaws.com', 'localhost:8000','3.224.227.254','138.2.94.85'] 
CSRF_TRUSTED_ORIGINS = ['https://*.inneedcloud.com','https://*.127.0.0.1','https://44.207.172.150','http://44.207.172.150','http://*.inneedcloud.com','https://0.0.0.0','https://apiipics.inneedcloud.com','http://apiipics.inneedcloud.com','https://testapi.inneedcloud.com','http://testapi.inneedcloud.com','https://3.224.227.254','http://3.224.227.254','http://138.2.94.85','https://138.2.94.85']

try:
    from .local import *
except ImportError:
    pass
