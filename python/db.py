import mysql.connector

from helper import config

con = {
    'host': config.get('database', 'host'),
    'user': config.get('database', 'user'),
    'passwd': config.get('database', 'password'),
    'db': config.get('database', 'db'),
    'port': config.get('database', 'port')
}

class db:

    config = {}

    def __init__(self, config):
        self.config = config


    def excute(self,sql,data):
        try:
            cnn = mysql.connector.connect(**self.config)
            cursor = cnn.cursor()
            cursor.execute(sql, data)
        except mysql.connector.Error as e:
            print('mysql fails!{}'.format(e))
        finally:
            cursor.close()
            cnn.close()

    def queryOne(self,sql_,data):
        try:
            cnn = mysql.connector.connect(**self.config)
            cursor = cnn.cursor()
            cursor.execute(sql_, data)
            row = cursor.fetchone()
            return row
        except mysql.connector.Error as e:
            print('mysql fails!{}'.format(e))
        finally:
            cursor.close()
            cnn.close()

