from config import app as application
from flask import render_template
from dotenv import load_dotenv

load_dotenv()


@application.route('/', methods=['GET'])
def index():
    return render_template('main.html')