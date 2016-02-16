# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
from django.views.decorators.cache import cache_page

# Local application / specific library imports


class CacheMixin(object):
    cache_timeout = 60

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)
