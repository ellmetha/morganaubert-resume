# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from morganaubert.sitemaps import MorganaubertViewSitemap
from morganaubert.views import HomeView


# Admin autodiscover
admin.autodiscover()

sitemaps = {
    'static': MorganaubertViewSitemap,
}

# Patterns
urlpatterns = [
    # Admin
    url(r'^' + settings.ADMIN_URL, include(admin.site.urls)),

    # Apps
    url(r'^$', HomeView.as_view(), name='home'),

    # Test 503, 500, 404 and 403 pages
    url(r'^403/$', TemplateView.as_view(template_name='403.html')),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    url(r'^503/$', TemplateView.as_view(template_name='503.html')),

    # Sitemaps
    url(r'^sitemap\.xml$', views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    # Robots
    url(r'^robots.txt$',
        TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]

if settings.DEBUG:
    # Add the Debug Toolbar’s URLs to the project’s URLconf
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

    # In DEBUG mode, serve media files through Django.
    urlpatterns += staticfiles_urlpatterns()
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns(
        '',
        url(r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
