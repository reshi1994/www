from functools import wraps

from pandas import DataFrame, concat

from .initDatabase import Init
from flask import request


class responseRegister(Init):
    api = '/login'
    need_keys = ['admin', 'userName', 'pwd']

    @staticmethod
    def get_need_data():
        data = request.get_json()
        # 数据不能为空
        if data is None:
            return {'res': False, 'print': '请求非法！！！'}
        # 请求行为必须正确
        need_data = {}
        for name in responseRegister.need_keys:
            value = data.get(name, None)
            if name == 'admin' and value is None:
                return {'res': False, 'print': '请选择用户登录类型！！！'}
            if not name == 'admin' and not value:
                return {'res': False, 'print': '缺少账户基本信息！！！'}
            need_data[name] = value

        return {'res': True, 'print': '', 'data': need_data}

    def get_register_users(self):
        df = self.open_table_index()
        return df

    def exists_user(self, userName):
        # 获取 总索引表
        df = self.get_register_users()
        # 空表说明没有用户；
        if df.empty:
            return {'res': False, 'print': '用户名不存在！！！'}

            # 查找用户
        df_row = df[df['userName'].apply(lambda x: True if f"{userName}" == f"{x}" else False)]
        # 多条记录者 取最后一行
        if len(df) > 1:
            df_row = df_row.iloc[-1:]
        if df_row.empty:
            return {'res': False, 'print': '用户名不存在！！！'}

        return {'res': True, 'print': '用户存在', 'data': df_row}

    @staticmethod
    def val_pwd(new_df_row, pwd):
        try:
            pwd_server = new_df_row.loc[:, 'pwd']
        except:
            return {'res': False, 'print': '服务器缺少密码！！！'}
        pwd_server = pwd_server.values[0]
        if not pwd_server:
            return {'res': False, 'print': '服务器密码出错！！！'}
        # print(type(pwd_server), type(pwd))
        if not f"{pwd_server}" == f"{pwd}":
            return {'res': False, 'print': '密码错误！！！'}
        return {'res': True, 'print': '密码校验通过！'}

    def val_login(self):
        # 判断 传送来的数据是否缺失
        res = self.get_need_data()
        if not res.get('res'):
            return res

        data = res.get('data')
        userName = data.get('userName')
        pwd = data.get('pwd')
        # 验证用户名是否存在
        res = self.exists_user(userName)
        if not res.get('res'):
            return res

        new_df_row = res.get('data')
        # 验证密码
        res = self.val_pwd(new_df_row, pwd)
        if not res.get('res'):
            return res

        return {'res': True, 'print': '用户登录成功！'}


# if  __name__ == '__main__':
#     register = responseRegister()
#     register.get_register_users()


def response_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = responseRegister().val_login()
        return res

        # print(res)
        # print(request.get_json())
        # if not res.get('res'):
        #     return res
        #
        # return {'res': True, 'data': res.get('data')}
        # return func(*args, **kwargs)

    return wrapper
