from config import app as application
from flask import render_template, request
import utils



@application.route('/', methods=['GET'])
def index():
    genre_response = utils.get_genres().get('genres')
    anime_response = utils.get_animes().get('documents')
    return render_template('main.jinja', genres=genre_response, animes=anime_response)

@application.route('/anime/<id>/<name>', methods=['GET'])
def detail(id: str, name: str):
    anime_id = int(id)
    anime_response = utils.get_specific_anime(anime_id)
    # return anime_response
    return render_template('detail_before_sub.jinja', anime=anime_response)

@application.route('/subscribe', methods=['GET','POST'])
def subsribe():
    if request.method == 'POST':
        data = request.form
        utils.make_subscription(data)
    return render_template('subscribe.jinja')