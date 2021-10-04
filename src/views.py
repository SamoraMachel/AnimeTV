from config import app as application
from flask import render_template, request
import utils



@application.route('/', methods=['GET'])
def index():
    genre_response = utils.get_genres().get('genres')
    anime_response = utils.get_animes().get('documents')
    genre_response.sort()
    return render_template('main.jinja',
                           genres=genre_response, animes=anime_response)

@application.route('/anime/<id>/<name>', methods=['GET'])
def detail(id: str, name: str):
    anime_id = int(id)
    anime_response = utils.get_specific_anime(anime_id)
    # anime_episodes = utils.get_anime_episode(anime_id)
    return render_template('detail_before_sub.jinja', anime=anime_response)

@application.route('/subscribe', methods=['GET','POST'])
def subsribe():
    if request.method == 'POST':
        data = request.form
        utils.make_subscription(data)
    return render_template('subscribe.jinja')

@application.route('/catalog', methods=['GET'])
def catalog():
    genre_response = utils.get_genres().get('genres')
    anime_response = utils.get_animes().get('documents')
    genre_response.sort()
    return render_template('catalog.jinja', 
                           genres=genre_response, animes=anime_response)

@application.route('/catalog/<genre>', methods=['GET'])
def catalog_genre(genre: str):
    genre_response = utils.get_genres().get('genres')
    anime_response = utils.get_animes_by_genre(genre).get('documents')
    genre_response.sort()
    return render_template('catalog.jinja', 
                           genres=genre_response, animes=anime_response) 