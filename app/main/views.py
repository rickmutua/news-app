from flask import render_template
from . import main
from ..requests import get_sources, get_source_articles
from flask_login import login_required

@main.route('/')
def index():

    general_sources = get_sources('general')

    business_source = get_sources('business')

    sport_source = get_sources('sport')

    politics_source = get_sources('politics')

    entertainment_source = get_sources('entertainment')

    technology_source = get_sources('technology')

    gaming_source = get_sources('gaming')

    music_source = get_sources('music')

    title = 'Welcome to News App, Your one stop for all news highlights'

    return render_template('index.html', title=title, general=general_sources, business=business_source,
                           sport=sport_source, politics=politics_source, entertainment=entertainment_source,
                           technology=technology_source, gaming=gaming_source, music=music_source)


@main.route('/source/<name>')
@login_required

def source(name):

    articles = get_source_articles(name)

    title = f'{name}'

    return render_template('source-articles.html', articles=articles, title=title, name=name)

#
# @app.route('/source/<source_id>/<article_id>')
# def article(article_id):
#
#     return render_template('articles.html', id = article_id)