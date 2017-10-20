from flask import render_template

from app import app

from .requests import get_sources


@app.route('/')
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


@app.route('/source/<source_id>')
def source(source_id):

    return render_template('source.html', id = source_id)