from functools import wraps
from .databaseOperate import Operate
from flask import request, session, jsonify, send_file, send_from_directory, url_for


class responseGtImage(Operate):
    imageAPI = 'getImage'

    @staticmethod
    def get_args_info():
        return dict(request.args)

    def val_users_get_action(self):
        args = self.get_args_info()
        # 不能不传参数
        if args is None:
            return {'res': False, 'print': '非法请求！！！'}
        # 请求行为必须正确
        path_for = args.get('for')
        name = args.get('name')

        # 必须有路径和文件名两个args
        if not path_for:
            return {'res': False, 'print': '缺少路径！！！'}
        if not name:
            return {'res': False, 'print': '缺少文件名！！！'}

        return {'res': True, 'print': '', 'args': args}

    def redirect_img_to_dst(self, path_for):
        # print(self.root_users)
        if path_for == 'users':
            return f"{self.root_users}"
        return ''

    def response_users_getImage(self):
        res = self.val_users_get_action()
        if not res.get('res'):
            return res
        # 验证并redirect 服务器的新地址；
        path_for = res.get('args').get('for')
        path_to = self.redirect_img_to_dst(path_for=path_for)
        name = res.get('args').get('name')
        dst = f"{path_to}/{name}.jpg"
        print(f"文件服务器地址: {dst}")
        return send_file(dst, mimetype='image')


def response_image(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return responseGtImage().response_users_getImage()
        # return func(*args, **kwargs)

    return wrapper
