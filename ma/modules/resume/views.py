"""
    Resume views
    ============

    This module defines the views responsible for exposing information for the resume website.

"""

import datetime as dt

from dateutil.relativedelta import relativedelta
from flask import Blueprint, render_template


resume_blueprint = Blueprint('resume', __name__)


@resume_blueprint.route('/', methods=['GET', ])
def home():
    """ The main entrypoint of the resume web application. """
    return render_template(
        'resume/home.html',
        age=relativedelta(dt.datetime.now(), dt.datetime(day=7, month=7, year=1989)).years,
    )
