from flask import Blueprint, jsonify, request
from ..source.responseRegister import response_register
register_blu = Blueprint('register', __name__)


@register_blu.route('/register', methods=['post', 'get'])
@response_register
def api():
    # return jsonify('register')
    pass


def load_register_blu(app):
    app.register_blueprint(register_blu)
