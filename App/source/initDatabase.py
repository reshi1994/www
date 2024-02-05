import sys
from os import makedirs
from os.path import exists, join, dirname
from pandas import DataFrame, read_csv
from pandas.errors import EmptyDataError
from datetime import datetime
import socket


class Init(object):
    host = f"http://{socket.gethostbyname(socket.gethostname())}"
    port = 5000
    root = f"{dirname(dirname(dirname(__file__)))}/database"
    root_dirs = ['users', 'patients']
    root_users = join(root, 'users')
    root_patients = join(root, 'patients')
    dst_table_index = join(root, 'index.table')
    encoding = 'utf-8'
    invitationCode = 'rehabs T'

    def __init__(self):
        print(f"database: {self.root}")
        pass

    def init_all(self):
        self.init_dirs()
        self.init_table_index()

    def gen_dirs(self):
        dirs = [f"{self.root}/{i}" for i in self.root_dirs]
        return dirs

    def init_dirs(self):
        for d in self.gen_dirs():
            if not exists(d):
                makedirs(d)

    def init_table_index(self):
        dst = self.dst_table_index
        if not exists(dst):
            file = DataFrame()
            file.to_csv(dst, encoding=self.encoding, index=False)

    def open_table_index(self):
        dst = self.dst_table_index
        try:
            df = read_csv(dst, encoding=self.encoding)
        except EmptyDataError:
            df = DataFrame()
        return df


if __name__ == '__main__':
    init = Init()
    init.init_all()
#     print(init.root_users)
# print(os.path.dirname(os.path.dirname(__file__)))
# print(Init.host, type(Init.host))
