from django.conf.urls import url
from django.contrib.sitemaps import views as sitemaps_views

from . import sitemaps
from . import views


sitemaps = {
    'static': sitemaps.MorganaubertViewSitemap,
}

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^sitemap\.xml$', sitemaps_views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]
