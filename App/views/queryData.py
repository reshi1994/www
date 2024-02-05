from flask import Blueprint, jsonify
from ..source.responseQueryData import response_data
query_data_blu = Blueprint('queryData', __name__)


@query_data_blu.route('/queryData', methods=['post', 'get'])
@response_data
def api():
    pass


def load_query_data_blu(app):
    app.register_blueprint(query_data_blu)
