import openai


class Open_IA():
	

	def __init__( self ):
		openai.api_key = 'Key_Token_Api'

	def responder_chat_open_ia( self , list_conversacion_previa ):
		#conversacion = list_conversacion_previa[0]
		#conversacion["tipo"] = "Human" | "AI"
		#conversacion["mensaje"] = "Buenos dias, este es el mensaje de respuesta a la IA"

		prompt_text = ""
		for conversacion in list_conversacion_previa: 
			prompt_text += f"{conversacion['tipo']}:{conversacion['mensaje']}\n"
		response = openai.Completion.create(
			model="text-davinci-003",
			prompt= prompt_text,
			temperature=0.9,
			max_tokens=150,
			top_p=1,
			frequency_penalty=0,
			presence_penalty=0.6,
			stop=[" Human:", " AI:"]
		)

		return response["choices"][0]["text"]

	def genera_imagen_ipen_ai( self , texto ):
		response = openai.Image.create(
			prompt= texto,
			n=1,
			size="256x256",
		)
		#['256x256', '512x512', '1024x1024']
		print( response['data'][0]['url'] )
		return response['data'][0]['url']

if __name__ == "__main__":
	openai.api_key = 'Key_Token_Api'
	obj_open_ai = Open_IA()
	'''
	list_conversacion_previa = []
	list_conversacion_previa.append( {"tipo":"Human" , "mensaje": "Buen dia Open_Ia" } )
	list_conversacion_previa.append( {"tipo":"AI" , "mensaje": "¡Buen día! ¿En qué puedo ayudarte?" } )
	list_conversacion_previa.append( {"tipo":"Human" , "mensaje": "Queria saber si puedes decirme la fecha actual" } )
	list_conversacion_previa.append( {"tipo":"AI" , "mensaje": "Hoy es miércoles, 17 de junio de 2020." } )
	list_conversacion_previa.append( {"tipo":"Human" , "mensaje": "A que temperatura un ser humano puede descansar en grados celcios" } )
	obj_open_ai.responder_chat_open_ia( list_conversacion_previa )
	'''
	obj_open_ai.genera_imagen_ipen_ai( "un gato" )