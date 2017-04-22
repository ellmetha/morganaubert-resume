from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.utils.timezone import get_default_timezone
from django.utils.timezone import make_aware
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.views.generic import TemplateView
from meta.views import MetadataMixin

from ma.common.viewmixins import CacheMixin


class HomeView(CacheMixin, MetadataMixin, TemplateView):
    template_name = 'morganaubert/home.html'
    cache_timeout = 60 * 15

    birdhday_date = datetime(day=7, month=7, year=1989)

    # Meta data
    title = _('Morgan Aubert')
    description = _('I am Morgan Aubert. A self taught, French born Software Engineer '
                    'with a focus on web development.')
    keywords = [
        'Morgan Aubert',
        ugettext('Interactive Resume'),
        ugettext('Software engineer'),
        ugettext('Python programmer'),
        ugettext('Python'),
        ugettext('Django'),
        ugettext('Web developer'),
        ugettext('Startup'),
        ugettext('CV'),
        ugettext('Resume'),
    ]

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['age'] = relativedelta(
            now(), make_aware(self.birdhday_date, get_default_timezone())).years
        context['current_year'] = now().year

        return context
