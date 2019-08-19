from flask import Blueprint,Flask,render_template
from App.models import Person


blue = Blueprint('mypro',__name__)

def init_blue(app:Flask):
    app.register_blueprint(blue)


@blue.route('/')
def index():
    return render_template('index.html')







