from flask_cors import CORS


def load_cors(app):
    CORS(app, supports_credentials=True)
