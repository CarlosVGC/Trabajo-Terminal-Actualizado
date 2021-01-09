from time import sleep
from random import randint
from time import time
from warnings import warn
from requests import get
from bs4 import BeautifulSoup
from IPython.core.display import clear_output
import pandas as pd
import os

nombres_frutas = []
precios_frutas = []
nombres_verduras = []
precios_verduras = []
nombres_lacteos = []
precios_lacteos = []
nombres_enlatados = []
nombres_carnes = []
precios_carnes = []
precios_enlatados = []


def extraerhbe(): #Funcion Obtiene datos de la pagina del comercio Lacomer
    #variables donde se guardaran los datos a obtener
   
    peticiones = 0
    tiempo_inicio = time()
    tipo_paginas =[i for i in range(0,5)] # 5 Tipos de página |0:frutas| |1:verduras| |2:lacteos| |3:carnes| |4:enlatados|

    pagina_frutas ='https://www.heb.com.mx/super/frutas-y-verduras/fruta?p='
    pagina_verduras = 'https://www.heb.com.mx/super/frutas-y-verduras/verdura?p='
    pagina_lacteos = 'https://www.heb.com.mx/super/lacteos?p='
    pagina_carnes = 'https://www.heb.com.mx/super/carnes-y-pescados?p='
    pagina_enlatados = 'https://www.heb.com.mx/super/abarrotes/enlatados-y-comida-instantanea?p=' 
    
    '''
    ----------------paginas donde se extrae la informacion de la seccion frutas----------------------
    https://www.heb.com.mx/super/frutas-y-verduras/fruta?p=1
    https://www.heb.com.mx/super/frutas-y-verduras/fruta?p=2
    
    ----------------paginas donde se extrae la informacion de la seccion verduras----------------------    
    https://www.heb.com.mx/super/frutas-y-verduras/verdura?p=1
    https://www.heb.com.mx/super/frutas-y-verduras/verdura?p=2
    
    ----------------paginas donde se extrae la informacion de la seccion lacteos----------------------
    https://www.heb.com.mx/super/lacteos?p=1
    https://www.heb.com.mx/super/lacteos?p=2
    
    ----------------paginas donde se extrae la informacion de la seccion carnes----------------------
    https://www.heb.com.mx/super/carnes-y-pescados?p=1
    https://www.heb.com.mx/super/carnes-y-pescados?p=2
    
    ----------------paginas donde se extrae la informacion de la seccion enlatados----------------------
    https://www.heb.com.mx/super/abarrotes/enlatados-y-comida-instantanea?p=1
    https://www.heb.com.mx/super/abarrotes/enlatados-y-comida-instantanea?p=2
    '''
    
    paginas = [str(i) for i in range(1,3)] 
    print(paginas)
    
    for tipo_pagina in tipo_paginas:
        #Se realiza un ciclo para cada una de las páginas
        nombres = []
        precios = []
        i=0
        for pagina in paginas:
            
            #Se realiza una petición según sea el caso
            if tipo_pagina == 0:
                response = get(pagina_frutas + pagina) 
          
            if tipo_pagina == 1:
                response = get(pagina_verduras + pagina)
    
            if tipo_pagina == 2:
                response = get(pagina_lacteos + pagina)
                i+= 1
                
            if tipo_pagina == 3:
                response = get(pagina_carnes + pagina)
                i+= 1
                
            if tipo_pagina == 4:
                response = get(pagina_enlatados + pagina)
                
            # Pausa la petición en un intervalo aleatorio de 5 a 8s para que no bloqueen la direccion IP 
            sleep(randint(4,6))
    
            # Monitoreando las peticiones
            peticiones += 1
            tiempo_transcurrido = time() - tiempo_inicio
            print('Peticion:{}; Frecuencia: {} peticiones/s'.format(peticiones, peticiones/tiempo_transcurrido))
            clear_output(wait = True)
    
            # Throw a warning for non-200 status codes
            if response.status_code != 200:
                warn('Request: {}; Status code: {}'.format(peticiones, response.status_code))
    
            # Break the loop if the number of requests is greater than expected
            if peticiones > 10:
                warn('Number of requests was greater than expected.')
                break
    
            # Parse the content of the request with BeautifulSoup
            html_soup = BeautifulSoup(response.text, 'html.parser')
    
            #Selecciona todos los contenedores de los precios de los productos
            contenedores_productos = html_soup.find_all('li', class_='item product product-item')
            
            for contenedor_nombre in contenedores_productos:
                nombres.append(contenedor_nombre.a['title'])
            
            # Selecciona todos los contenedores de los precios de los productos
            for contenedor_precio in contenedores_productos:
                precios.append(contenedor_precio.find('span', class_ = 'price').get_text(strip = True)) # .get_text(strip = True) quita los espacios \xa0 al final de la cadena 
            
            
        correcion_datos_hbe(nombres, precios, tipo_pagina) #Se llama a la funcion para corregir los datos obtenidos

def correcion_datos_hbe(nombres, precios, tipo_pagina):
    
    #Quitando los simbolos $ y convirtiendo en flotante los precios
    i=0
    for precio in precios:
        precios[i] = float((precio.strip('$')).replace(',',''))
        i+=1
    
    i=0
    for nombre in nombres:
        nombres[i] = nombre.replace(u'\xa0', u'')  # remueve completamente todos los \xa0
        nombres[i] = nombre.title()
        i+=1
    
    if tipo_pagina == 0:
        # Poniendo la info en pandas
        global nombres_frutas
        global precios_frutas
        
        nombres_frutas = nombres[:101]
        precios_frutas = precios[:101]
        
        Info_frutas = pd.DataFrame({'Fruta': nombres,
                                      'Precio': precios
                                    })
        print(Info_frutas)
        
        archivo = pd.read_csv("csv/infofrutas.csv") #Se lee el archivo
        archivo['Frutas HBE'] = nombres_frutas[:60] 
        archivo['Precio Frutas HBE'] = precios_frutas[:60]
        archivo.to_csv('csv/infofrutas.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 1:
        # Poniendo la info en pandas
        global nombres_verduras
        global precios_verduras
        
        nombres_verduras = nombres[:101]
        precios_verduras = precios[:101]
                  
        Info_verduras = pd.DataFrame({'Verdura': nombres,
                                      'Precio': precios
                                    })
        print(Info_verduras)
        
        archivo = pd.read_csv("csv/infoverduras.csv") #Se lee el archivo
        archivo['Verduras HBE'] = nombres_verduras[:60] 
        archivo['Precio Verduras HBE'] = precios_verduras[:60]
        archivo.to_csv('csv/infoverduras.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 2:
        # Poniendo la info en pandas
        global nombres_lacteos
        global precios_lacteos
        
        nombres_lacteos = nombres[:101]
        precios_lacteos = precios[:101]
                  
        Info_lacteos = pd.DataFrame({'Lacteo': nombres,
                                      'Precio': precios
                                    })
        print(Info_lacteos)
        
        archivo = pd.read_csv("csv/infolacteos.csv") #Se lee el archivo
        archivo['Lacteos HBE'] = nombres_lacteos[:60] 
        archivo['Precio Lacteos HBE'] = precios_lacteos[:60]
        archivo.to_csv('csv/infolacteos.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 3:
        # Poniendo la info en pandas
        global nombres_carnes
        global precios_carnes
        
        nombres_carnes = nombres[:101]
        precios_carnes = precios[:101]
        
        Info_carnes = pd.DataFrame({'Carne': nombres,
                                      'Precio': precios
                                    })
        print(Info_carnes)
        
        archivo = pd.read_csv("csv/infocarnes.csv") #Se lee el archivo
        archivo['Carnes HBE'] = nombres_carnes[:60] 
        archivo['Precio Carnes HBE'] = precios_carnes[:60]
        archivo.to_csv('csv/infocarnes.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 4:
        # Poniendo la info en pandas          
        global nombres_enlatados
        global precios_enlatados
        
        nombres_enlatados = nombres[:101]
        precios_enlatados = precios[:101]
        
        
        Info_enlatados = pd.DataFrame({'Enlatados': nombres,
                                      'Precio': precios
                                    })
        print(Info_enlatados)
        
        archivo = pd.read_csv("csv/infoenlatados.csv") #Se lee el archivo
        archivo['Enlatados HBE'] = nombres_enlatados[:60] 
        archivo['Precio Enlatados HBE'] = precios_enlatados[:60]
        archivo.to_csv('csv/infoenlatados.csv',encoding = 'utf8',index=False)
        
        info_hbe = pd.DataFrame({'Frutas':  nombres_frutas,
                                 'Precio Frutas': precios_frutas,
                                 'Verdura':nombres_verduras,
                                 'Precio Verduras': precios_verduras,
                                 'Lacteos':nombres_lacteos,
                                 'Precio Lacteos': precios_lacteos,
                                 'Carne': nombres_carnes,
                                 'Precio Carnes':precios_carnes,
                                 'Enlatados ':nombres_enlatados,
                                 'Precio Enlatados': precios_enlatados
                                 })
        
        crearuta = r'csv' #ruta a crear carpeta
        if not os.path.exists(crearuta): os.makedirs(crearuta) # creacion de la carpeta
    
        info_hbe.to_csv('csv/info_hbe.csv', encoding = 'utf8')
        