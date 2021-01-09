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


def datossor(): # Funcion donde se guardan los datos de Soriana
    #variables donde se guardaran los datos a obtener
    peticiones = 0
    tiempo_inicio = time()
    tipo_paginas =[i for i in range(0,5)] #0,5 Tipo de página |0:frutas| |1:verduras| |2:lacteos| |3:carnes| |4:enlatados|

    pagina_frutas ='https://superentucasa.soriana.com/default.aspx?P=13' #287,616,319
    pagina_verduras = 'https://superentucasa.soriana.com/default.aspx?P=132' #88, 86, 64
    pagina_lacteos = 'https://superentucasa.soriana.com/default.aspx?p=132' #92,91,89
    pagina_carnes = 'https://superentucasa.soriana.com/default.aspx?P=132' # 72, 69, 67
    pagina_enlatados = 'https://superentucasa.soriana.com/default.aspx?P=132' #42,52,56
    
    '''
    ----------------paginas donde se extrae la informacion de la seccion frutas----------------------
    https://superentucasa.soriana.com/default.aspx?P=13287
    https://superentucasa.soriana.com/default.aspx?P=13616
    https://superentucasa.soriana.com/default.aspx?P=13319
    
    ----------------paginas donde se extrae la informacion de la seccion verduras----------------------
    https://superentucasa.soriana.com/default.aspx?P=13288
    https://superentucasa.soriana.com/default.aspx?P=13286
    https://superentucasa.soriana.com/default.aspx?P=13264
    
    ----------------paginas donde se extrae la informacion de la seccion lacteos----------------------
    https://superentucasa.soriana.com/default.aspx?p=13292
    https://superentucasa.soriana.com/default.aspx?P=13291
    https://superentucasa.soriana.com/default.aspx?P=13289
    
    ----------------paginas donde se extrae la informacion de la seccion carnes----------------------
                ----res-----
    https://superentucasa.soriana.com/default.aspx?P=13272
    https://superentucasa.soriana.com/default.aspx?P=13269
    https://superentucasa.soriana.com/default.aspx?P=13267
    
    ----------------paginas donde se extrae la informacion de la seccion enlatados----------------------
    https://superentucasa.soriana.com/default.aspx?P=13242
    https://superentucasa.soriana.com/default.aspx?p=13252
    https://superentucasa.soriana.com/default.aspx?P=13256
    '''
    
    paginas = ['287','616','319','88','86','64','92','91','89','72','69','67','42','52','56'] # 1,4 Se extraen los datos de las primeras 3 paginas 24*3 72 datos aproximadamente 
    print(paginas)
    
    for tipo_pagina in tipo_paginas:
        #Se realiza un ciclo para cada una de las páginas
        nombres = []
        precios = []
        for i in range(0,3):
            #Se realiza una petición según sea el caso
            if tipo_pagina == 0:
                response = get(pagina_frutas + paginas[peticiones]) 
            if tipo_pagina == 1:
                response = get(pagina_verduras + paginas[peticiones])
    
            if tipo_pagina == 2:
                response = get(pagina_lacteos + paginas[peticiones])
                
            if tipo_pagina == 3:
                response = get(pagina_carnes + paginas[peticiones])
                
            if tipo_pagina == 4:
                response = get(pagina_enlatados + paginas[peticiones])
                
            # Pausa la petición en un intervalo aleatorio de 2 a 5s para que no bloqueen la direccion IP 
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
    
            # Selecciona todos los contenedores de los precios de los productos     col-md-12 col-sm-6 col-xs-6 
            contenedores_nombres = html_soup.find_all('div', class_='col-lg-3 col-md-4 col-sm-12 col-xs-12 product-item')
            
            for contenedor_nombre in contenedores_nombres:
                nombres.append(contenedor_nombre.h4.get_text(strip = True))
            
            
                
            # Selecciona todos los contenedores de los precios de los productos
            contenedores_precios = html_soup.find_all('div', class_='precios-plp plp-item-div')
            for contenedor_precio in contenedores_precios:
                precios.append(contenedor_precio.get_text(strip = True)) # .get_text(strip = True) quita los espacios \xa0 al final de la cadena 
            
            
       
        correccion_datos_sor(precios, nombres, tipo_pagina)



def correccion_datos_sor(precios, nombres, tipo_pagina):
    
    i=0
    
    for precio in precios:
        precios[i] =float(precio[-5:].strip('$'))
        #float(precio.strip('$'))
        i+=1
        
        
    i=0
    for nombre in nombres:
        nombres[i] = nombre.replace(u'\xa0', u'')  # removed completely \xa0
        i+=1
    
    if tipo_pagina == 0:
        # Poniendo la info en pandas
        global nombres_frutas
        global precios_frutas
    
        nombres_frutas = nombres[:61]
        precios_frutas = precios[:61]
        
        Info_frutas = pd.DataFrame({'Fruta': nombres,
                                      'Precio': precios
                                    })
        print(Info_frutas)
        
        archivo = pd.read_csv("csv/infofrutas.csv") #Se lee el archivo
        archivo['Frutas Soriana'] = nombres_frutas[:60] 
        archivo['Precio Frutas Soriana'] = precios_frutas[:60]
        archivo.to_csv('csv/infofrutas.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 1:
        # Poniendo la info en pandas
        global nombres_verduras
        global precios_verduras
        
        nombres_verduras = nombres[:61]
        precios_verduras = precios[:61]
        Info_verduras = pd.DataFrame({'Verdura': nombres,
                                      'Precio': precios
                                    })
        print(Info_verduras)
        
        archivo = pd.read_csv("csv/infoverduras.csv") #Se lee el archivo
        archivo['Verduras Soriana'] = nombres_verduras[:60] 
        archivo['Precio Verduras Soriana'] = precios_verduras[:60]
        archivo.to_csv('csv/infoverduras.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 2:
        # Poniendo la info en pandas
        global nombres_lacteos
        global precios_lacteos
        
        nombres_lacteos = nombres[:61]
        precios_lacteos = precios[:61]
        Info_lacteos = pd.DataFrame({'Lacteo': nombres,
                                      'Precio': precios
                                    })
        print(Info_lacteos)
        
        archivo = pd.read_csv("csv/infolacteos.csv") #Se lee el archivo
        archivo['Lacteos Soriana'] = nombres_lacteos[:60] 
        archivo['Precio Lacteos Soriana'] = precios_lacteos[:60]
        archivo.to_csv('csv/infolacteos.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 3:
        # Poniendo la info en pandas
        global nombres_carnes
        global precios_carnes
        
        nombres_carnes = nombres[:61]
        precios_carnes = precios[:61]        
        Info_carnes = pd.DataFrame({'Carne': nombres,
                                      'Precio': precios
                                    })
        print(Info_carnes)
        
        archivo = pd.read_csv("csv/infocarnes.csv") #Se lee el archivo
        archivo['Carnes Soriana'] = nombres_carnes[:60] 
        archivo['Precio Carnes Soriana'] = precios_carnes[:60]
        archivo.to_csv('csv/infocarnes.csv',encoding = 'utf8',index=False)
        
    if tipo_pagina == 4:
        # Poniendo la info en pandas
        global nombres_enlatados
        global precios_enlatados
        
        nombres_enlatados = nombres[:61]
        precios_enlatados = precios[:61]
        
        Info_enlatados = pd.DataFrame({'Enlatados': nombres,
                                      'Precio': precios
                                    })
        print(Info_enlatados)
        
        archivo = pd.read_csv("csv/infoenlatados.csv") #Se lee el archivo
        archivo['Enlatados Soriana'] = nombres_enlatados[:60] 
        archivo['Precio Enlatados Soriana'] = precios_enlatados[:60]
        archivo.to_csv('csv/infoenlatados.csv',encoding = 'utf8',index=False)
        
        info_sor = pd.DataFrame({'Frutas':  nombres_frutas,
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
        
        info_sor.to_csv('csv/info_sor.csv', encoding = 'utf8')




