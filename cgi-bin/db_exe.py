from multiprocessing import Process
from multiprocessing import Lock
import sqlite3
mutex = Lock()
class db_exe():
    def __init__(self):
        self.con = sqlite3.connect("./account.db")
        self.cur = self.con.cursor()

    def account_table(self):
        try:
            self.cur.execute("""CREATE TABLE account (
                        name text, password text, familyname text, firstname text, age text);""")
            return True
        except:
            return False

    def account_data_insert(self,name, password):
        ac_list = self.cur.execute("""SELECT name,password FROM account;""")
        for ac,pw in ac_list:
            if ac == name:
                return "This account created already"
        self.cur.execute("""INSERT INTO account(name, password) VALUES('%s', '%s')""" % (name, password))
        self.con.commit()

        ac_list = self.cur.execute("""SELECT name,password FROM account;""")
        for ac,pw in ac_list:
            if (ac == name) and (pw == password):
                return "Create successfull"
        return "Account create fail"

    def account_check(self,username, password):
        ac_list = self.cur.execute("""SELECT name,password FROM account;""")
        for ac,pw in ac_list:
            if (ac == username) and (pw == password):
                return True
        return False

    def account_create_check(self,username):
        ac_list = self.cur.execute("""SELECT name FROM account;""")
        for ac in ac_list:
            if ac == username:
                return True
        return False

    def account_get_check(self,username):
        ac_list = self.cur.execute("""SELECT * FROM account;""")
        for info in ac_list:
            if info[0] == username:
                return info
        raise Exception('account check NG')

    def account_info_update(self, string, username):
        self.cur.execute("""UPDATE account SET %s WHERE name = %s""" % (string, username))

