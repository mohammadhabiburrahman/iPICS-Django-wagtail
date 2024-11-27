from argparse import Namespace
from unicodedata import name
from django.conf import settings
from django.urls import include, path , re_path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
# from wagtail.documents import urls as wagtaildocs_urls

from django.contrib.auth.decorators import login_required
from ckeditor_uploader.views import upload

from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views



from search import views as search_views
urlpatterns = [
    # path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    # path('documents/', include(wagtaildocs_urls)),

    # path('search/', search_views.search, name='search'),
    path('api/',include('ipicsAPI.urls'),),
    re_path(r'^chaining/', include('smart_selects.urls')),
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r'^ckeditor/upload/', login_required(upload), name='ckeditor_upload'),
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
    re_path(r'^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
else:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]

