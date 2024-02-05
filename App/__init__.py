from flask import Flask
from .views.queryData import load_query_data_blu
from .views.getImage import load_get_image_blu
from .config import load_app_setting


def create_app():
    app = Flask(__name__)
    # 加载配置文件
    load_app_setting(app)
    # 加载路由
    load_query_data_blu(app)
    load_get_image_blu(app)

    return app

