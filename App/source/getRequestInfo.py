from functools import wraps
from flask import request


class Base(object):
    """
    request, session 在类初始化的时候，一定要填入，否则后续信息的提取会报错
    类属性设置 和 初始化__init__ 中的 self.类属性的区别：类属性是全局，即类属性值的变化 和 import 包 相关联，如果不重新导入包，那么这个值就不会改变；
    如果要每次类 实例化的时候，这个值改变的话，那么需要在初始化 __init__ 的时候重新赋值；
    """
    @staticmethod
    def get_header():
        return dict(request.headers)

    @staticmethod
    def get_ip():
        return request.remote_addr

    @staticmethod
    def get_user_agent():
        return request.user_agent.string

    @staticmethod
    def get_method():
        return request.method

    @staticmethod
    def get_path():
        return request.path

    @staticmethod
    def get_request_header():
        client_ip = request.remote_addr
        user_agent = request.user_agent.string
        method = request.method
        path = request.path
        headers = dict(request.headers)
        cookies = dict(request.cookies)

        client_header = {
            'client_ip': client_ip,
            'user_agent': user_agent,
            'method': method,
            'path': path,
            'headers': headers,
            'cookies': cookies
        }
        return client_header

    @staticmethod
    def get_post_info():
        req = request.get_json()
        return req

    @staticmethod
    def get_query_info():
        return dict(request.args)

    @staticmethod
    def get_form_data():
        return dict(request.form)


if __name__ == '__main__':
    val = Base()


def pass_options(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'OPTIONS':
            return 'CORS localhost:8080 通过！'
        return func(*args, **kwargs)

    return wrapper
