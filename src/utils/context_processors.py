# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
from django.contrib.sites.models import Site

# Local application / specific library imports


def site(request):
    return {
        'site': Site.objects.get_current()
    }
