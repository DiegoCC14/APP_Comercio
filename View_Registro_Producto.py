import sys

from PyQt5 import uic #Carga la interfaz  grafica
from PyQt5.QtWidgets import QMainWindow , QApplication , QDialog

class Registro_Productos_App( QMainWindow ): #Reemplazo de 'QMainWindow' por 'QDialog'
								 #Depende del tipo de ventana a renderizar
	def __init__(self):
		super().__init__()
		uic.loadUi( 'Interfaz_Registro_Productos.ui' , self )

		self.Boton_Limpiar_Campos.clicked.connect( self.Borrar_Campos )
		
		self.Boton_Validar_Campos.clicked.connect( self.Verificar_Campos )
		
		#self.Boton_Registrar_Producto.clicked.connect( self.Abrir_Ventana_Registro_Producto )

	def Borrar_Campos(self):

		self.Entrada_Nombre_Producto.setText("")
		self.Entrada_Precio_Interno_Producto.setText("")
		self.Entrada_Precio_Venta_Producto.setText("")
		self.Entrada_Codigos_Barras.setText("")

		self.Valido_Nombre_Producto.setText("")
		self.Valido_Precio_Interno_Producto.setText("")
		self.Valido_Precio_Venta_Producto.setText("")
		self.Valido_Codigo_Barra_Producto.setText("")

	def Verificar_Campos(self):
		self.Entrada_Nombre_Producto.toPlainText()
		self.Entrada_Precio_Interno_Producto.toPlainText()
		self.Entrada_Precio_Venta_Producto.toPlainText()
		self.Entrada_Codigos_Barras.toPlainText()

app_Registro = QApplication( sys.argv )

Aplicacion = Registro_Productos_App()
Aplicacion.show()

sys.exit( app_Registro.exec_() )