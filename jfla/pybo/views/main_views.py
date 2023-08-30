from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

import random
from flask import render_template

@bp.route('/hello')
def hello_pybo():

    abab = random.randint(1, 100)
    print(abab)
    print(3)

    return render_template('question/new.html', club = abab)

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
