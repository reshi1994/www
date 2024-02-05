from functools import wraps

from pandas import DataFrame,concat

from .initDatabase import Init
from flask import request


class responseRegister(Init):
    api = '/register'
    table_names = ['account', 'personal']

    @staticmethod
    def get_need_data():
        data = request.get_json()
        # 数据不能为空
        if data is None:
            return {'res': False, 'print': '请求非法！！！'}
        # 请求行为必须正确
        need_data = []
        for name in responseRegister.table_names:
            table = data.get(name, None)
            if not table:
                return {'res': False, 'print': '缺少账户基本信息！！！'}
            need_data.append(table)

        return {'res': True, 'print': '', 'data': need_data}

    @staticmethod
    def trans_need_data(need_data):
        result = {}
        for table in need_data:
            for key in table.keys():
                table[key] = [table[key].get('value', '')]
            result.update(table)

        return result

    def get_register_users(self):
        df = self.open_table_index()
        return df

    def get_userNameValue(self):
        data = request.get_json()

    def is_registered(self, userNameValue):
        # 获取 总索引表
        df = self.get_register_users()
        # 空表说明没有用户；可以直接注册；非空表的话，看看表里有没有用户
        if not df.empty:
            df = df[df['userName'].apply(lambda x: True if f"{userNameValue}" == f"{x}" else False)]
            if not df.empty:
                return {'res': False, 'print': '用户已存在！'}

        return {'res': True, 'print': '用户可以注册！'}

    def create_user_df(self):
        # 判断请求数据是否合理
        res = self.get_need_data()
        if not res.get('res'):
            return res
        # 转化数据，并新建一个 DataFrame对象
        need_data = res.get('data')
        need_data = self.trans_need_data(need_data)
        # print(need_data)
        new_df_row = DataFrame.from_dict(need_data, orient='columns')
        return {'res': True, 'print': '创建用户成功！', 'data': new_df_row}

    def val_userName(self, new_df_row):
        try:
            userNameValue = new_df_row.loc[:, 'userName']
        except:
            return {'res': False, 'print': '缺少用户名！！！'}

        userNameValue = userNameValue.values[0]
        if not userNameValue:
            return {'res': False, 'print': '请输入用户名！！！'}
        return {'res': True, 'print': '用户名校验成功！', 'data': userNameValue}

    def val_pwd_pwd2(self, new_df_row):
        try:
            pwd = new_df_row.loc[:, 'pwd']
        except:
            return {'res': False, 'print': '缺少密码！！！'}
        pwd = pwd.values[0]
        if not pwd:
            return {'res': False, 'print': '请输入密码！！！'}

        try:
            pwd2 = new_df_row.loc[:, 'pwd2']
        except:
            return {'res': False, 'print': '缺少确认密码！！！'}
        pwd2 = pwd2.values[0]
        if not pwd2:
            return {'res': False, 'print': '请再次输入密码！！！'}

        if not pwd ==pwd2:
            return {'res': False, 'print': '两次密码不匹配！！！'}
        return {'res': True, 'print': '密码校验通过！'}

    def val_register(self):
        # 尝试创建用户；过程中会自动判断 用户信息是否合理
        res = self.create_user_df()
        if not res.get('res'):
            return res

        new_df_row = res.get('data')

        # 验证用户名
        res = self.val_userName(new_df_row)
        if not res.get('res'):
            return res

        userNameValue = res.get('data')
        # 验证是否可以注册
        res = self.is_registered(userNameValue)
        if not res.get('res'):
            return res

        # 验证密码
        res = self.val_pwd_pwd2(new_df_row)
        if not res.get('res'):
            return res



        # print(new_df_row)
        # noinspection PyUnresolvedReferences
        # try:
        #     userNameValue = new_df_row.loc[:, 'userName']
        # except:
        #     return {'res': False, 'print': '缺少用户名！！！'}
        #
        # userNameValue = userNameValue.values[0]
        # if not userNameValue:
        #     return {'res': False, 'print': '请输入用户名！！！'}

        # 合并原注册表和新的对象
        df = self.open_table_index()
        df = concat([df, new_df_row])
        dst = self.dst_table_index
        try:
            df.to_csv(dst, index=False, encoding=self.encoding)
        except:
            return {'res': False, 'print': '注册信息保存失败，请稍后再试！！！'}
        return {'res': True, 'print': '用户注册成功！'}

# if  __name__ == '__main__':
#     register = responseRegister()
#     register.get_register_users()


def response_register(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = responseRegister().val_register()
        return res

        # print(res)
        # print(request.get_json())
        # if not res.get('res'):
        #     return res
        #
        # return {'res': True, 'data': res.get('data')}
        # return func(*args, **kwargs)

    return wrapper
