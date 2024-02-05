from flask import Blueprint, send_file, jsonify, request
from ..source.responseGetImage import response_image
get_image_blu = Blueprint('getImage', __name__)


@get_image_blu.route('/getImage', methods=['get'])
@response_image
def get_image():
    pass


def load_get_image_blu(app):
    app.register_blueprint(get_image_blu)
