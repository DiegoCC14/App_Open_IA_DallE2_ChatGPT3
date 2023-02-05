from pathlib import Path
from urllib.parse import urlparse

import requests , shutil , os # request img from web


BASE_DIR = Path(__file__).resolve().parent #Direccion actual


def obtener_nobre_imagen( url_imagen ):
    return os.path.basename( urlparse( url_imagen ).path ) #Nombre.formato imagen

def descarga_lista_imagenes( lista_imagenes , dir_carpeta ):

    for dicc_imagen in lista_imagenes:
        try:
            reponse = requests.get( dicc_imagen["url"] , stream = True )
            if reponse.status_code == 200:
                with open( dir_carpeta/dicc_imagen["nombre"] ,'wb' ) as file:
                    shutil.copyfileobj( reponse.raw , file )
                dicc_imagen["descargado"] = True
            else:
                dicc_imagen["descargado"] = False
        except:
            dicc_imagen["descargado"] = False
    
    return lista_imagenes

if __name__ == "__main__":
        
    lista_imagenes = []

    dicc_imagen = {}
    dicc_imagen["url"] = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-fy8GwnuXBTVtR1wxUhgk8ye4/user-JRGRYAgObzUQiEPP3jAZVymz/img-MoXro87ZxdxmIy8BFceci5Cv.png?st=2023-02-05T13%3A58%3A03Z&se=2023-02-05T15%3A58%3A03Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-04T23%3A32%3A25Z&ske=2023-02-05T23%3A32%3A25Z&sks=b&skv=2021-08-06&sig=gt85HOybOYL%2BmwUYcLDum58RnMuBATyWWjGL3fmGfmo%3D'
    dicc_imagen["nombre"] = obtener_nobre_imagen('https://oaidalleapiprodscus.blob.core.windows.net/private/org-fy8GwnuXBTVtR1wxUhgk8ye4/user-JRGRYAgObzUQiEPP3jAZVymz/img-MoXro87ZxdxmIy8BFceci5Cv.png?st=2023-02-05T13%3A58%3A03Z&se=2023-02-05T15%3A58%3A03Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-04T23%3A32%3A25Z&ske=2023-02-05T23%3A32%3A25Z&sks=b&skv=2021-08-06&sig=gt85HOybOYL%2BmwUYcLDum58RnMuBATyWWjGL3fmGfmo%3D')
    lista_imagenes.append(dicc_imagen)
    descarga_lista_imagenes( lista_imagenes , BASE_DIR/'Imagenes' )