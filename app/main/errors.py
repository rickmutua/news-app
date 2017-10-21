from flask import render_template

from . import main


@main.app_errorhandler(404)
def four_0w_four(error):

    return render_template('four0wfour.html'), 404