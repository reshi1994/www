from flask import Flask
from .views.register import load_register_blu
from .views.login import load_login_blu
from .config import load_app_setting


def create_app():
    app = Flask(__name__)
    # 加载配置文件
    load_app_setting(app)
    # 加载路由
    load_register_blu(app)
    load_login_blu(app)
    return app

