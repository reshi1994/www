from functools import wraps
from .databaseOperate import Operate
from flask import request


class responseQueryData(Operate):

    @staticmethod
    def val_post_action(req_action):
        data = request.get_json()
        # 数据不能为空
        if data is None:
            return {'res': False, 'print': '请求非法！！！'}
        # 请求行为必须正确
        action = data.get('action')
        if not action:
            return {'res': False, 'print': '请求非法！！！'}

        if not action == req_action:
            return {'res': False, 'print': '请求非法！！！'}
        return {'res': True, 'print': '', 'action': action}

    def get_users_all(self):
        df = self.find_users_all()
        df_members = df.loc[:, ['user', 'surName', 'givenName', 'imgSrc']]
        return df_members

    def gen_users_imgSrc(self, df):

        host = f"{self.host}:{str(self.port)}/getImage"
        df.loc[:, 'imgSrc'] = df['user'].apply(lambda x: f"{host}?for=users&name={x}")
        return df

    def response_teams(self):
        # 验证action
        res = self.val_post_action('queryTeamMembers')
        if not res.get('res'):
            return res

        try:
            df = self.get_users_all()
            # 产生正确get 接口的请求地址
            df = self.gen_users_imgSrc(df)
            # 以列表的形式 转化记录；没有记录则为[]
            records_list = df.to_dict(orient='records')
            return {'res': True, 'data': records_list}
        except:
            return {'res': False, 'print': '数据获取失败！！！'}


def response_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = responseQueryData().response_teams()
        if not res.get('res'):
            return res

        return {'res': True, 'data': res.get('data')}
        # return func(*args, **kwargs)

    return wrapper
