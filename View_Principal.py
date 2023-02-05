import pathlib , sys

from PyQt5.Qt import *
from PyQt5 import uic , QtWidgets  #Carga la interfaz  grafica
from PyQt5.QtWidgets import QMainWindow , QApplication , QDialog , QFileDialog , QTableWidgetItem , QLabel
from PyQt5.QtCore import QFile, QTextStream , QThread , Qt
from PyQt5.QtGui import QPixmap

from threading import Thread

BASE_DIR = pathlib.Path( 'Vista_Principal.ui' ).parent.absolute()

class Inicio_App( QMainWindow ):

	controller_principal = None

	def __init__(self , Controller ):

		super().__init__()
		uic.loadUi( 'View_Principal.ui' , self )

		self.controller_principal = Controller
		
		self.cargar_tabla_historial_mensaje()
		self.actualizar_tabla_historial_de_mensajes()

		# Acciones Button ---------------------->>>>>>>>>>>>>>>
		self.Button_Enviar_Mensaje.clicked.connect( self.enviar_mensaje )
		self.Button_Generar_Imagen.clicked.connect( self.obtener_imagen_Dall_E_2 )
		# -------------------------------------->>>>>>>>>>>>>>>

	# Asistente AI OPEN IA
	#=========================================>>>>>>>>>>>>>>>>>>>>>

	def cargar_tabla_historial_mensaje( self ):
		self.Qtable_Historial_Conversacion.setRowCount( 100 )
		self.Qtable_Historial_Conversacion.setColumnCount( 2 )
		self.Qtable_Historial_Conversacion.setHorizontalHeaderLabels( ['Tipo' , 'Mensaje'] )

		self.Qtable_Historial_Conversacion.setColumnWidth( 0 , 55 )
		self.Qtable_Historial_Conversacion.setColumnWidth( 1 , 365 )

	def actualizar_tabla_historial_de_mensajes( self ):

		self.eliminar_filas_Tabla_historial_mensajes()
		
		list_contactos = self.controller_principal.obtiene_historial_mensajes()

		for fila , contacto in enumerate( list_contactos[::-1] ):
			self.Qtable_Historial_Conversacion.setItem( fila , 0 , QTableWidgetItem( str( contacto["tipo"] ) ) )
			self.Qtable_Historial_Conversacion.setItem( fila , 1 , QTableWidgetItem( str( contacto["mensaje"] ) ) )

	def eliminar_filas_Tabla_historial_mensajes( self ):
		for fila in range( self.Qtable_Historial_Conversacion.rowCount() ):
			for columna in range( self.Qtable_Historial_Conversacion.columnCount() ):
				self.Qtable_Historial_Conversacion.setItem( fila , columna , None )

	def enviar_mensaje( self ):
		texto_mensaje = self.Qtext_Mensaje.toPlainText()
		self.controller_principal.enviar_mensaje_humano_a_asistente_AI( texto_mensaje )
		self.actualizar_tabla_historial_de_mensajes()
		
	#=========================================>>>>>>>>>>>>>>>>>>>>>
	
	def obtener_imagen_Dall_E_2( self ):
		descripcion_imagen = self.Qtext_Descripcion_Imagen.toPlainText()
		dir_imagen = self.controller_principal.obtener_imagen_segun_descripcion_Dall_E_2( descripcion_imagen )
		self.pixmap = QPixmap( dir_imagen )
		self.label_Imagen_OpenAI.setPixmap( self.pixmap )

	#=========================================>>>>>>>>>>>>>>>>>>>>>

if __name__ == "__main__":
	app = QApplication( sys.argv )
	#obj_controller = Controller_Principal.Controller_Princiapal()

	Aplicacion = Inicio_App()
	Aplicacion.setFixedSize( 520 , 600 ) #759
	Aplicacion.show()

	sys.exit( app.exec_() )

