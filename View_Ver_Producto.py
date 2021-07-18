import sys

from PyQt5 import uic #Carga la interfaz  grafica
from PyQt5.QtWidgets import QMainWindow , QApplication , QDialog

class Registro_Productos_App( QMainWindow ): #Reemplazo de 'QMainWindow' por 'QDialog'
								 #Depende del tipo de ventana a renderizar
	def __init__(self):
		super().__init__()
		uic.loadUi( 'Interfaz_Ver_Producto.ui' , self )

		self.Boton_Buscar.clicked.connect( self.Buscar_Producto )
		
		#self.Boton_Validar_Campos.clicked.connect( self.Verificar_Campos )
		
		#self.Boton_Registrar_Producto.clicked.connect( self.Abrir_Ventana_Registro_Producto )

	def Buscar_Producto(self):

		Codigo_Barras = self.Entrada_Codigo_Producto.toPlainText()
		self.Lista_Detalles_Producto.clear() #Borramos la lista
		self.Lista_Detalles_Producto.addItems([Codigo_Barras , Codigo_Barras , Codigo_Barras]) #Aniadimos los campos a la lista

app_Ver_Producto = QApplication( sys.argv )

Aplicacion = Registro_Productos_App()
Aplicacion.show()

sys.exit( app_Ver_Producto.exec_() )