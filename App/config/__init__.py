from .app_settings import *
from .cors import *


def load_app_setting(app):
    load_app_config(app)
    load_cors(app)