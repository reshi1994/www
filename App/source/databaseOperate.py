from os.path import join
from .databaseCreate import Init
from pandas import read_csv


class Operate(Init):

    def open_users_base(self):
        dst = join(self.root_users, 'users.base')
        df = read_csv(dst, encoding=self.encoding)
        return df

    def find_users_base(self, username):
        df = self.open_users_base()
        df_find = df[df['user'].apply(lambda x: True if username == f"{x}" else False)]
        if not df_find.empty:
            df_find = df_find.iloc[-1, :]
        return df_find

    def find_users_all(self):
        df = self.open_users_base()
        df = df.drop_duplicates(subset=['user'], keep='last')
        return df
# if __name__ == '__main__':
#     init = Init()
#     print(init.root_users)
