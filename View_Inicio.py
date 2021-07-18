import os
import sys

from PyQt5 import uic #Carga la interfaz  grafica
from PyQt5.QtWidgets import QMainWindow , QApplication , QDialog

class Inicio_App( QDialog ): #Reemplazo de 'QMainWindow' por 'QDialog' no se la difeencia 

	def __init__(self):
		super().__init__()
		uic.loadUi( 'Interfaz_Prueba.ui' , self )

		self.Boton_Registrar_Producto.clicked.connect( self.Abrir_Ventana_Registro_Producto )

	def Abrir_Ventana_Registro_Producto(self):
		#self.Boton_Registrar_Producto.setEnabled(False)
		os.system('python View_Registro_Producto.py') #Usando Python en Ubuntu sera Python3
		

app = QApplication( sys.argv )

Aplicacion = Inicio_App()
Aplicacion.show()

sys.exit( app.exec_() )