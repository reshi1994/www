from datetime import timedelta
init_settings = {
    'HOST': '0.0.0.0',
    'PORT': 5000,
    'DEBUG': True,
    'SECRET_KEY': '5f71bbf5dc987d54727823',
    'SERVER_NAME': None,
    'SESSION_COOKIE_NAME': 'session',
    # 当浏览器设置samesite 属性时，需要 Secure为true; 但是仍然被浏览器阻止存储在本地，所以更改为设置为false; 此时浏览器可以存储在本地；
    'SESSION_COOKIE_SECURE': False,
    # 'SESSION_COOKIE_SAMESITE': 'None',

    'PERMANENT_SESSION_LIFETIME': timedelta(minutes=10),
    'MAX_CONTENT_LENGTH': None,
    'UPLOAD_FOLDER': None,
    'MAX_COOKIE_SIZE': 4093,
    'TEMPLATES_AUTO_RELOAD': False,
    # 添加其他配置项...

}


def load_app_config(app):
    app.config.update(**init_settings)
