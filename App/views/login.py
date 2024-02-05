from flask import Blueprint, jsonify, request
from ..source.responseLogin import response_login
login_blu = Blueprint('login', __name__)


@login_blu.route('/login', methods=['post', 'get'])
@response_login
def api():
    # return jsonify('register')
    pass


def load_login_blu(app):
    app.register_blueprint(login_blu)
