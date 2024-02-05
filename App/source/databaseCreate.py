import sys
from os import makedirs
from os.path import exists, join, dirname
from pandas import DataFrame
from datetime import datetime
import socket


class Init(object):
    host = f"http://{socket.gethostbyname(socket.gethostname())}"
    port = 5000
    root = f"{dirname(dirname(dirname(__file__)))}/database"
    root_dirs = ['users', 'patients']
    root_users = join(root, 'users')
    root_patients = join(root, 'patients')
    encoding = 'utf-8'
    invitationCode = 'rehabs T'

    def __init__(self):
        print(f"database: {self.root}")
        pass

    def init_all(self):
        self.init_dirs()
        self.init_table_users_base()
        self.init_table_users_patients()

    def gen_dirs(self):
        dirs = [f"{self.root}/{i}" for i in self.root_dirs]
        return dirs

    def init_dirs(self):
        for d in self.gen_dirs():
            if not exists(d):
                makedirs(d)

    @staticmethod
    def super_user():
        super_user = {'user': 'RehabsTerc', 'pwd': 'reshi', 'surName': 'Rehabs', 'givenName': 'Terc',
                      'title': 'Resident Physician', 'imgSrc': '',
                      "createTime": datetime.now()}
        return super_user

    def init_table_users_base(self):
        dst = f"{self.root}/users/users.base"
        if not exists(dst):
            file = DataFrame(columns=['user', 'pwd', 'surName', 'givenName', 'title', 'imgSrc', 'createTime'])
            super_user = self.super_user()
            file.loc[len(file)] = super_user
            file.to_csv(dst, encoding=self.encoding, index=False)

    def init_table_users_patients(self):
        dst = f"{self.root}/users/users.patients"
        if not exists(dst):
            file = DataFrame(
                columns=['user', 'uniqueID', 'name', 'age', 'gender', 'bed', 'diagnosis', 'status', 'admissions'])
            file.to_csv(dst, encoding=self.encoding, index=False)


# if __name__ == '__main__':
#     init = Init()
#     print(init.root_users)
# print(os.path.dirname(os.path.dirname(__file__)))
# print(Init.host, type(Init.host))
