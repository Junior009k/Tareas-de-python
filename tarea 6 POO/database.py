#import mysql.connector
nombre=[]
edad=[]
print("Resultados de MySQLdb:")

def cargaBaseDeDatos():
    #miConexion =  mysql.connector.connect( host='localhost', user= 'root', passwd='root', db='mydb',auth_plugin='mysql_native_password')
    #cur = miConexion.cursor()
    #cur.execute( "SELECT nombre, edad FROM Alumnos" )
    #for n, e in cur.fetchall() :
    #    nombre.append(n)
    #    edad.append(e)
    #    print (n, e)
    #
    #miConexion.close()
    nombre.append("a")
    edad.append("a")
    return nombre,edad
cargaBaseDeDatos()

def hello():
	return "world"