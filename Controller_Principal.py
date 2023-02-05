import pathlib , sys , json
import View_Principal
from services.Open_AI_service import Open_IA
from services.download_image_service import obtener_nobre_imagen , descarga_lista_imagenes

from PyQt5.QtWidgets import QApplication



BASE_DIR = pathlib.Path( 'View_Principal.ui' ).parent.absolute()


class Controller_Principal():

	vista_principal = None

	def __init__( self ):
		pass
		self.inicindo_vista_principal()


	def inicindo_vista_principal( self ):
		app = QApplication( sys.argv )
		self.vista_principal = View_Principal.Inicio_App( self )
		self.vista_principal.setFixedSize( 541 , 590 ) #759
		self.vista_principal.show()
		sys.exit( app.exec_() )

	def obtiene_historial_mensajes( self ):
		#Puede ser obtenida de una DB o un archivo JSON, Tomaremos JSON esta vez
		file_historial_mensaje = open("historial_mensajes.json","r")
		return [ { "tipo":conversacion["tipo"] , "mensaje":conversacion["mensaje"] } for conversacion in json.load( file_historial_mensaje ) ]

	def enviar_mensaje_humano_a_asistente_AI( self , text_mensaje ):
		list_historial_conversacion = self.obtiene_historial_mensajes()
		list_historial_conversacion.append( { "tipo":"Human" , "mensaje": text_mensaje } )
		self.agregar_registro_a_historial_mensajes( { "tipo":"Human" , "mensaje": text_mensaje } ) 
		respuesta_text_AI = Open_IA().responder_chat_open_ia( list_historial_conversacion )
		respuesta_text_AI = respuesta_text_AI.replace("AI:" , "").replace("Robot:","").replace("IA:","").strip()
		self.agregar_registro_a_historial_mensajes( { "tipo":"AI" , "mensaje": respuesta_text_AI } )

	def agregar_registro_a_historial_mensajes( self , conversacion ):
		with open( "historial_mensajes.json" , 'r+' ) as file:
			file_data = json.load(file)			
			file_data.append( conversacion )
			file.seek(0)
			json.dump( file_data , file , indent=4 )

	def obtener_imagen_segun_descripcion_Dall_E_2( self , description_imagen ):
		url_imagen = Open_IA().genera_imagen_ipen_ai( description_imagen )
		nombre_imagen = obtener_nobre_imagen( url_imagen )
		lista_imagenes = descarga_lista_imagenes( [{"url": url_imagen ,"nombre": nombre_imagen } ] , BASE_DIR/'imagenes' )
		return ( str( BASE_DIR/f'imagenes/{nombre_imagen}' ) )


if __name__ == "__main__":
	obj_controller = Controller_Principal()