import psycopg2, psycopg2.extras
import pymysql
import cx_Oracle

class Conexion():
    
    def __init__(self, motor_db, user, passwd, port, host):
        
        self.motor_db = motor_db
        self.user = user
        self.passwd = passwd
        self.port = port
        self.host = host

    def validar_conexion(self):
        if self.motor_db == 'mysql':
            config_mysql = {
                'user': self.usuario,
                'passwd': self.contrasena,
                'host': self.ip_servidor,
                'port': self.puerto,
                }
            try:
                conn = pymysql.connect(**config_mysql)
                return True
            except:
                return False

        if self.motor_db == 'postgresql':
            pass

        if self.motor_db == 'oracle':
            pass
        