import mysql.connector

def Abrir_Conexion():
	#Conecta con la Base de Datos ( DB [Data Base])
	''' 
	-h brzq0rsktp2der07uwg0-mysql.services.clever-cloud.com 
	-P 3306 
	-u uney766i2wqkm0an 
	-DB brzq0rsktp2der07uwg0
	PASSWORD: pHCSKl7UIq57Di9Qurc1
	'''
	return mysql.connector.connect(
		host="brzq0rsktp2der07uwg0-mysql.services.clever-cloud.com",
		password="pHCSKl7UIq57Di9Qurc1",
		user="uney766i2wqkm0an",
		port="3306",
		db="brzq0rsktp2der07uwg0"
		) #Retorna la conexion establecida

def Cerrar_Conexion( sql ):
	sql.close()

def Ver_Tablas_de_DB( sql ):
	# sql: mysql.cursor -> Siendo mysql la conexion con DB [primero>Abrir_Conexion()]
	# -->> Retorna una lista con todas las tablas de DB
	cur = sql.cursor()
	try:
		cur.execute("SHOW TABLES")
		return( list( cur.fetchall() ) ) #Retorna una lista con todas las filas de DB
	except:
		print("<<<----- NO SE VE TABLAS DE LA DB [error]->[func: Ver_Tabla()] ----->>>")

def Ver_Tabla( sql , Nombre_Tabla ):
	# sql: mysql.cursor -> Siendo mysql la conexion con DB [primero>Abrir_Conexion()]
	# Nombre_Tabla: Nombre de la Tabla a ver
	# -->> Retorna una tupla con todas las filas de DB
	cur = sql.cursor()
	try:
		cur.execute("SELECT * FROM " + Nombre_Tabla)
		return( list( cur.fetchall() ) ) #Retorna una lista con todas las filas de DB
	except:
		print("<<<----- SIN ACCESO A TABLA: " + Nombre_Tabla + "  [error]->[func: Ver_Tabla()] ----->>>")

def Ver_Campos_Tabla( sql , Nombre_Tabla ):
	# Retorna los campos de la Tabla
	# sql: mysql.cursor -> Siendo mysql la conexion con DB [primero>Abrir_Conexion()]
	# Nombre_Tabla: Nombre de la Tabla a ver DESCRIPCION
	# -->> Retorna una tupla con todas las filas de DB
	cur = sql.cursor()
	try:
		cur.execute("DESCRIBE " + Nombre_Tabla)
		return( list( cur.fetchall() )) #Retorna una lista con todos los Campos de DB
	except:
		print("<<<----- SIN ACCESO A TABLA: " + Nombre_Tabla + "  [error]->[func: Ver_Campos_Tabla()] ----->>>")




SQL = Abrir_Conexion()
#Ver_Campos_Tabla( SQL,"Productos" )
#Ver_Tablas_de_DB( SQL )
Cerrar_Conexion( SQL )