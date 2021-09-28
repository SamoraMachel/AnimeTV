from config import app as application
from flask import render_template
import utils



@application.route('/', methods=['GET'])
def index():
    return utils.get_genres()
    # return render_template('main.html')