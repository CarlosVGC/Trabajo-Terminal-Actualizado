from time import sleep
from random import randint
from time import time
from warnings import warn
from requests import get
from bs4 import BeautifulSoup
#from urllib.request import Request, urlopen
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

def datosche(): #Funcion Obtiene datos de la pagina del comercio Chedraui
    #variables donde se guardaran los datos a obtener
   
    peticiones = 0
    tiempo_inicio = time()
    tipo_paginas =[i for i in range(0,5)] # 5Tipo de página |0:frutas| |1:verduras| |2:lacteos| |3:carnes| |4:enlatados|

    pagina_frutas ='https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Frutas/c/MC210101?q=%3Arelevance&page='
    pagina_verduras = 'https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Verduras/c/MC210102?q=%3Arelevance&page='
    pagina_lacteos = 'https://www.chedraui.com.mx/Departamentos/Súper/Lácteos-y-Huevos/c/MC2104?q=%3Arelevance&page='
    pagina_carnes = 'https://www.chedraui.com.mx/Departamentos/Súper/Carnes%2C-aves%2C-pescados-y-mariscos/c/MC2102?q=%3Arelevance&page='
    pagina_enlatados = 'https://www.chedraui.com.mx/Departamentos/Súper/Despensa/Enlatados-y-Conservas/c/MC210510?q=%3Arelevance&page='
    
    '''
    ----------------paginas donde se extrae la informacion de la seccion frutas----------------------
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Frutas/c/MC210101?q=%3Arelevance&page=0&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Frutas/c/MC210101?q=%3Arelevance&page=1&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Frutas/c/MC210101?q=%3Arelevance&page=2&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Frutas/c/MC210101?q=%3Arelevance&page=3&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Frutas/c/MC210101?q=%3Arelevance&page=4&pageSize=24
    
    ----------------paginas donde se extrae la informacion de la seccion verduras----------------------
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Verduras/c/MC210102?q=%3Arelevance&page=0&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Verduras/c/MC210102?q=%3Arelevance&page=1&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Verduras/c/MC210102?q=%3Arelevance&page=2&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Verduras/c/MC210102?q=%3Arelevance&page=3&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Frutas-y-Verduras/Verduras/c/MC210102?q=%3Arelevance&page=4&pageSize=24
    
    ----------------paginas donde se extrae la informacion de la seccion lacteos----------------------
    https://www.chedraui.com.mx/Departamentos/Súper/Lácteos-y-Huevos/c/MC2104?q=%3Arelevance&page=0&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Lácteos-y-Huevos/c/MC2104?q=%3Arelevance&page=1&pageSize=24
    
    ----------------paginas donde se extrae la informacion de la seccion carnes----------------------
    https://www.chedraui.com.mx/Departamentos/Súper/Carnes%2C-aves%2C-pescados-y-mariscos/c/MC2102?q=%3Arelevance&page=0&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Carnes%2C-aves%2C-pescados-y-mariscos/c/MC2102?q=%3Arelevance&page=1&pageSize=24
    
    ----------------paginas donde se extrae la informacion de la seccion enlatados----------------------
    https://www.chedraui.com.mx/Departamentos/Súper/Despensa/Enlatados-y-Conservas/c/MC210510?q=%3Arelevance&page=0&pageSize=24
    https://www.chedraui.com.mx/Departamentos/Súper/Despensa/Enlatados-y-Conservas/c/MC210510?q=%3Arelevance&page=1&pageSize=24
    '''
    
    paginas = [str(i) for i in range(0,3)] #()Se extraen los datos de las primeras 5 paginas 24*5 100 a 120 datos 
    print(paginas)
    
    for tipo_pagina in tipo_paginas:
        #Se realiza un ciclo para cada una de las páginas
        nombres = []
        precios = []
        for pagina in paginas:
            
            #Se realiza una petición según sea el caso
            if tipo_pagina == 0:
                response = get(pagina_frutas + pagina + '&pageSize=24') #pagina de chedraui
          
            
            if tipo_pagina == 1:
                response = get(pagina_verduras + pagina + '&pageSize=24')
    
            if tipo_pagina == 2:
                response = get(pagina_lacteos + pagina + '&pageSize=24')
                
            if tipo_pagina == 3:
                response = get(pagina_carnes + pagina + '&pageSize=24')
                
            if tipo_pagina == 4:
                response = get(pagina_enlatados + pagina + '&pageSize=24')
                
            # Pausa la petición en un intervalo aleatorio de 8 a 15s para que no bloquen la direccion IP 
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
            if peticiones > 15:
                warn('Number of requests was greater than expected.')
                break
    
            # Parse the content of the request with BeautifulSoup
            html_soup = BeautifulSoup(response.text, 'html.parser')
    
            # Selecciona todos los contenedores de los precios de los productos      
            precios_frutas = html_soup.find_all('div', class_='product__listing--price price-colour-final')
            
            for precio_fruta in precios_frutas:
                precios.append(precio_fruta.get_text(strip = True))
                
            # Selecciona todos los contenedores de los precios de los productos
            nombres_frutas = html_soup.find_all('a', class_='product__list--name')
            for nombre_fruta in nombres_frutas:
                nombres.append(nombre_fruta.get_text(strip = True)) # .get_text(strip = True) quita los espacios \xa0 al final de la cadena 
            
        correcion_datos_che(nombres, precios, tipo_pagina) #Se llama a la funcion para corregir los datos obtenidos

def correcion_datos_che(nombres, precios, tipo_pagina):
    
    #Eliminando los precios duplicados de la lista
    for i in range(0, len(precios)):
        del(precios[i])
        i+=2
        if(i > len(precios)):
            break
    #Quitando los simbolos $ y convirtiendo en flotante los precios
    i=0
    for precio in precios:
        precios[i] = float((precio.strip('$')).replace(',',''))
        i+=1
    
    i=0
    for nombre in nombres:
        nombres[i] = nombre.replace(u'\xa0', u'')  # removed completely \xa0
        i+=1
    
    if tipo_pagina == 0:
        # Poniendo la info en pandas
        global nombres_frutas
        global precios_frutas
        
        nombres_frutas = nombres[:71]
        precios_frutas = precios[:71]
        
        Info_frutas = pd.DataFrame({'Fruta': nombres,
                                      'Precio': precios
                                    })
        print(Info_frutas)
        
        archivo = pd.read_csv("csv/infofrutas.csv") #Se lee el archivo
        archivo['Frutas Chedraui'] = nombres_frutas[:60] 
        archivo['Precio Frutas Chedraui'] = precios_frutas[:60]
        archivo.to_csv('csv/infofrutas.csv',encoding = 'utf8',index=False)
    
        
    if tipo_pagina == 1:
        # Poniendo la info en pandas          
        global nombres_verduras
        global precios_verduras
        
        nombres_verduras = nombres[:71]
        precios_verduras = precios[:71]
        
        Info_verduras = pd.DataFrame({'Verdura': nombres,
                                      'Precio': precios
                                    })
        print(Info_verduras)
        
        archivo = pd.read_csv("csv/infoverduras.csv") #Se lee el archivo
        archivo['Verduras Chedraui'] = nombres_verduras[:60] 
        archivo['Precio Verduras Chedraui'] = precios_verduras[:60]
        archivo.to_csv('csv/infoverduras.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 2:
        # Poniendo la info en pandas

        global nombres_lacteos
        global precios_lacteos
        
        nombres_lacteos = nombres[:71]
        precios_lacteos = precios[:71]
        
        Info_lacteos = pd.DataFrame({'Lacteo': nombres,
                                      'Precio': precios
                                    })
        print(Info_lacteos)
        
        archivo = pd.read_csv("csv/infolacteos.csv") #Se lee el archivo
        archivo['Lacteos Chedraui'] = nombres_lacteos[:60] 
        archivo['Precio Lacteos Chedraui'] = precios_lacteos[:60]
        archivo.to_csv('csv/infolacteos.csv',encoding = 'utf8',index=False)
        
        
    if tipo_pagina == 3:
        # Poniendo la info en pandas

        global nombres_carnes
        global precios_carnes
        
        nombres_carnes = nombres[:71]
        precios_carnes = precios[:71]    
        
        Info_carnes = pd.DataFrame({'Carne': nombres,
                                      'Precio': precios
                                    })
        print(Info_carnes)
        
        archivo = pd.read_csv("csv/infocarnes.csv") #Se lee el archivo
        archivo['Carnes Chedraui'] = nombres_carnes[:60] 
        archivo['Precio Carnes Chedraui'] = precios_carnes[:60]
        archivo.to_csv('csv/infocarnes.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 4:
        # Poniendo la info en pandas

        global nombres_enlatados
        global precios_enlatados
        
        nombres_enlatados = nombres[:71]
        precios_enlatados = precios[:71]
        
        Info_enlatados = pd.DataFrame({'Enlatados': nombres,
                                      'Precio': precios
                                    })
        print(Info_enlatados)
        
        archivo = pd.read_csv("csv/infoenlatados.csv") #Se lee el archivo
        archivo['Enlatados Chedraui'] = nombres_enlatados[:60] 
        archivo['Precio Enlatados Chedraui'] = precios_enlatados[:60]
        archivo.to_csv('csv/infoenlatados.csv',encoding = 'utf8',index=False)
        
        info_che = pd.DataFrame({'Frutas':  nombres_frutas,
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
        
        info_che.to_csv('csv/info_che.csv', encoding = 'utf8')

