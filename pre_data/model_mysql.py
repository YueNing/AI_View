###############################
# Author: Yue Ning
# Datum: 10.01.2019
# Location: KIT
# File_Name: module_mysql
# E-mail: n1085633848@gmail.com
###############################

import os, sys
import pymysql 

class Module_mysql():
    def __init__(self, con):
        self._connection = pymysql.connect(host=con['host'],
                                user=con['user'], 
                                password=con['password'], 
                                db=con['db'], 
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        self._cursor = self._connection.cursor()

    @property
    def connection(self):
        return self._connection
    @property
    def cursor(self):
        return self._cursor

    def __exit__(self):
        self.commit()
        self.connection.close()

    def __enter__(self):
        return self

    def commit(self):
        self.connection.commit()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def insertTable(self, table_name, inserted_array):
        inserted = False
        insert_val = response = []
        if table_name:
            keys = ''
            values = ''
            for key, value in inserted_array.items():
                keys += "`" + key + "`,"
                values += "'"+value +"'," 
                insert_val.append(value)
            keys = keys[:-1]
            values = values[:-1]
            sql = "INSERT INTO " +"`" +table_name + "` " + "("+ keys + ")" + " VALUES " + "(" + values + ")"
            #import pdb
            #pdb.set_trace()
            self.query(sql)
            self.commit()
            inserted = True

if __name__ == '__main__':
    con = {'host':'localhost',
            'user':'mk_user',
            'password':'n865445399',
            'db':'mk'
            }
    db = Module_mysql(con)
    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    test_sql = "INSERT INTO `users` (`email`,`password`) VALUES ('test@email.com','test12345')"
    params = ('uqveo@student.kit.edu')
    db.query(sql, params=params)
    result = db.fetchone()
    print(result)
    inserted_array = {"email":"test@email.com", "password":"test12345"}
    db.insertTable('users', inserted_array)
    db.query(sql, params=('test@email.com'))
    #db.commit()
    result = db.fetchall()
    print(result)
