###############################
# Author: Yue Ning
# Datum: 10.01.2019
# Date last modified: 22/1/2019
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

    def insertTable(self, table_name='', inserted_array={}):
        inserted = False
        response = {}
        if table_name:
            keys = ''
            values = ''
            for key, value in inserted_array.items():
                keys += "`" + key + "`,"
                values += "'"+value +"'," 
            keys = keys[:-1]
            values = values[:-1]
            sql = "INSERT INTO " +"`" +table_name + "` " + "("+ keys + ")" + " VALUES " + "(" + values + ")"
            self.query(sql)
            self.commit()
            inserted = True
        if inserted:
            response = {"message": "inserted successfully"}
        else:
            response = {"message": "problem occured by inserted"}
        return response
    
    def deleteTable(self, table_name='', where_att={}):
        delete = False
        reponse = {}
        where_str = ''
        if table_name:
            for key, value in where_att.items():
                where_str += " and `" + key + "` =" + "'" + value + "'"
            sql = "DELETE FROM `" + table_name +"` where 1 " + where_str
            self.query(sql)
            self.commit()
            delete = True
        if delete:
            response = {"message": "delete successfully"}
        else:
            response = {"message": "problem occured by delete"}
        return response

    def updateTable(self, table_name='', update_val={}, where_att={}):
        update = False
        reponse = {}
        where_str = ''
        collum_str = ''
        if table_name:
            for key, value in update_val.items():
                collum_str += "`"+key+"` ='" +value+"',"
            collum_str = collum_str[:-1]
            if where_att:
                for key, value in where_att.items():
                    where_str +=" and `"+key+"`='"+value+"'"
            sql = "UPDATE "+table_name+" SET "+collum_str+" where 1 "+where_str
            self.query(sql)
            self.commit()
            update = True
        else:
            response = {"message":"provide valid table name"}
            return response
        if update:
            response = {"message":"update successfully"}
        else:
            response = {"message":"unknow error"}
        return response

if __name__ == '__main__':
    con = {'host':'localhost',
            'user':'mk_user',
            'password':'n865445399',
            'db':'mk'
            }
    db = Module_mysql(con)
    sql = "SELECT `id`, `password`,`email` FROM `users` WHERE `password`=%s"
    test_sql = "INSERT INTO `users` (`email`,`password`) VALUES ('test@email.com','test12345')"
    params = ('test123456')
    db.query(sql, params=params)
    result = db.fetchone()
    print(result)
    inserted_array = {"email":"test@email.com", "password":"test12345"}
    response = db.updateTable(table_name='users', update_val={"email":"n1085633848@outlook.com","password":"test123456"}, where_att={"password":"123456test"})
    print(response)
    db.query(sql, params=('test123456'))
    result = db.fetchall()
    print(result)
