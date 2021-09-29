from config import app as application
from flask import render_template
import utils



@application.route('/', methods=['GET'])
def index():
    genre_response = utils.get_genres().get('genres')
    anime_response = utils.get_animes().get('documents')
    return render_template('main.html', genres=genre_response, animes=anime_response)

@application.route('/anime/<id>/<name>', methods=['GET'])
def detail(id: str, name: str):
    return '%r %r' % (name, id)