import psycopg2, psycopg2.extras
import pymysql
import cx_Oracle

class Conectar:

    def __init__(self, usuario, contrasena, puerto, ip_servidor):

        self.ip_servidor = ip_servidor
        self.usuario = usuario 
        self.contrasena =  contrasena
        self.puerto = int(puerto) 

    # Para conectar a PostgreSQL
    def conectarPostgres(self):
        bds=[]
        try:    
            self.db_host = host
            self.db_user = usuario 
            self.db_pass = pss 
            self.db_port = port  
      
            conn = psycopg2.connect(user=self.db_user,password=self.db_pass,host=self.db_host,port=self.db_port)
      
            cursor = conn.cursor() 

            sql="SELECT datname FROM pg_database PD,pg_user PU WHERE usename= '%s' AND PD.datdba=PU.usesysid" %(usuario)
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:
                bds.append(row[0])
        except:
            bds=['error postgres'+ ' ' +self.db_user + ' '+ self.db_pass + ' '+ self.db_host + ' '+ self.db_port]
            #bds=['error postgres']

        return bds
        cursor.close ()
        conn.close()

    # Para conectar a MySQL
    def conectarMysql(self):
        bds=[]
        try:      
            self.db_host = host
            self.db_user = usuario 
            self.db_pass = pss 
            self.db_port = port 
      
            #conn = MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=int(self.db_port))
            conn = pymysql.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=int(self.db_port))
            #conn = mysql.connector.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=self.db_port)
            cursor = conn.cursor() 
            sql="show databases" 
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:
                bds.append(row[0])
                
        except Exception as inst:
            #bds=['error mysql'+ ' '+ self.db_host + ' '+  self.db_user + ' '+ self.db_pass + ' '+  self.db_port]
            bds=['error mysql' + str(inst)]

        cursor.close ()
        conn.close()
        return bds
  
    #Para conectar a Oracle
    def conectarOracle(self):
        bds=[]
        try:
            self.db_user = usuario 
            self.db_pass = pss 
            self.db_host = host
      
            s=str(self.db_user+"/"+self.db_pass+"@"+self.db_host)
            conn=cx_Oracle.connect(s)
  
            cursor = conn.cursor() 
            sql="select * from all_users" 
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:
                bds.append(row[0])
        except Exception as inst:
            bds=['error oracle' + str(inst) ]
        cursor.close ()
        conn.close()
        return bds
          
        
    #Ejecutar servicios
    def ejecutarServicios(self, sql, db, motor):
        estudiantes=[]
        try:      
            db_db = db
            db_sql = sql   
            if(motor=="postgres"):
                conn = psycopg2.connect(database=self.db_db,user=self.db_user,password=self.db_pass,host=self.db_host,port=self.db_port)
            elif(motor=="mysql"):
                conn = pymysql.connect(host=self.ip_servidor,user=self.usuario,passwd=self.contrasena,port=self.puerto,db=self.db_db)
            elif(motor=="oracle"):                     
                s=str(self.db_user+"/"+self.db_pass+"@"+self.db_host)
                conn=cx_Oracle.connect(s)
                
            cursor = conn.cursor() 
            sql=self.db_sql

            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:                        
                estudiantes.append(row)
            
        except Exception as inst:
            
            estudiantes=['error postgres----->'+ ' ' +self.db_user + ' '+ self.db_pass + ' '+ self.db_host + ' '+ self.db_port]
        return estudiantes

    def validar_conexion_mysql(self):
        config_mysql = {
            'user': self.usuario,
            'passwd': self.contrasena,
            'host': self.ip_servidor,
            'port': self.puerto,
        }
        print(config_mysql)
        try:
            conn = pymysql.connect(**config_mysql)
            return True
        except:
            return False

    def listar_db_mysql(self):
        config_mysql = {
            'user': self.usuario,
            'passwd': self.contrasena,
            'host': self.ip_servidor,
            'port': self.puerto,
        }
        try:           
            #conn = MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=int(self.db_port))
            conn = pymysql.connect(**config_mysql)
            #conn = mysql.connector.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=self.db_port)
            cursor = conn.cursor() 
            sql="show databases" 
            cursor.execute(sql)
            datos = [row[0] for row in cursor.fetchall()]
            print(datos)
            return datos
                          
        except Exception as inst:
            return None

        cursor.close ()
        conn.close()
        return bds
         