import mysql.connector

def Abrir_Conexion():
	#Conecta con la Base de Datos ( DB [Data Base])
	''' 
	-h brzq0rsktp2der07uwg0-mysql.services.clever-cloud.com 
	-P 3306 
	-u uney766i2wqkm0an 
	-DB brzq0rsktp2der07uwg0
	PASSWORD: pHCSKl7UIq57Di9Qurc1

	<<--CONEXION DESDE TERMINAL MYSQL-->>
	#mysql -h brzq0rsktp2der07uwg0-mysql.services.clever-cloud.com -P 3306 -u uney766i2wqkm0an -p brzq0rsktp2der07uwg0
	#Password: pHCSKl7UIq57Di9Qurc1
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

def Decodificar_UTF8(Cadena_Byte):
	# Parece que llegan bytes de la DB remota 
	# decodificamos los datos.
	# cuando la DB se encuentra en la misma PC no hace falta decodificar
	return( Cadena_Byte.decode("utf-8") )
	
def Decodificar_Arreglo(Arreglo_Bynario):
	Arreglo_Decodificado = []
	#print( type( Arreglo_Bynario[0][0] ) )
	for elemento_array in Arreglo_Bynario:
		print( 'Array: ',elemento_array )
		for elemento in elemento_array:
			print( 'Sub array: ',elemento )
			Arreglo_Decodificado.append( Decodificar_UTF8(elemento) )
	return Arreglo_Decodificado

def Ver_Tablas_de_DB( sql ):
	# sql: mysql.cursor -> Siendo mysql la conexion con DB [primero>Abrir_Conexion()]
	# -->> Retorna una lista con todas las tablas de DB
	cur = sql.cursor()
	cur.execute("SHOW TABLES;")
	return Decodificar_Arreglo( cur.fetchall() )
	#return( cur.fetchone()[0].decode("utf-8") ) 

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

def Insert_SQL( sql , Nombre_Tabla , Diccionario_Campos ):
	#sql: objeto con conexion establecida en DB
	#Nombre_Tabla: Nombre de la tabla a Insertar
	#Diccionario_Campos: Diccionario para ingresar a la Tabla	
	cur = sql.cursor()

	Campos_Tabla = '('
	for Campo in Diccionario_Campos.keys():
		Campos_Tabla += Campo + ','
	Campos_Tabla = Campos_Tabla[0:len(Campos_Tabla)-1] + ')'

	cur.execute("INSERT INTO " + Nombre_Tabla + tupla( Diccionario_Campos.keys() + " VALUES " + Diccionario_Campos.values() ) ) 
	cur.commit() #Guardamos los cambios

SQL = Abrir_Conexion()
#print( Ver_Campos_Tabla( SQL,"Productos" ) )
print( Ver_Tablas_de_DB( SQL ) )
Cerrar_Conexion( SQL )

Campos = {'Nombre_Producto':'Gaseosa',
		'Precio':125.50,
		'Precio Publico':200}

#Insert_SQL( 'algo' , 'Productos' , Campos )