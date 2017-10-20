from flask import render_template

from app import app


@app.route('/')
def index():

    return render_template('index.html')



@app.route('/source/<source_id>')
def source(source_id):

    return render_template('source.html', id = source_id)