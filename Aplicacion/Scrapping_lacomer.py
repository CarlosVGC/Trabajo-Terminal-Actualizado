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


def extraerlacomer(): #Funcion Obtiene datos de la pagina del comercio Lacomer
    #variables donde se guardaran los datos a obtener
   
    peticiones = 0
    tiempo_inicio = time()
    tipo_paginas =[i for i in range(0,5)] # 5 Tipos de página |0:frutas| |1:verduras| |2:lacteos| |3:carnes| |4:enlatados|

    pagina_frutas = 'https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=287&padreId=14&pasId=13&opcion=listaproductos&path=,14&pathPadre=0&jsp=PasilloPadre.jsp&noPagina='
    pagina_verduras = 'https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=287&padreId=15&pasId=13&opcion=listaproductos&path=,15&pathPadre=0&jsp=PasilloPadre.jsp&noPagina='
    pagina_lacteos = ['https://www.lacomer.com.mx/lacomer/doHome.action?key=Lácteos-Congelados-y-Huevo&succId=287&padreId=27&pasId=21&opcion=listaproductos&path=,27&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=2&mov=1&subOpc=0&agruId=21&succFmt=100&dep=Bebidas-lácteas-y-Orgánicos',
                      'https://www.lacomer.com.mx/lacomer/doHome.action?dep=Cremas-y-Natas&key=Lácteos-Congelados-y-Huevo&padreId=25&pasId=21&opcion=listaproductos&path=,25&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=21&succFmt=100',
                      'https://www.lacomer.com.mx/lacomer/doHome.action?dep=Huevo-blanco&key=Lácteos-Congelados-y-Huevo&padreId=1188&pasId=21&opcion=listaproductos&path=,1188&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=21&succFmt=100',
                      'https://www.lacomer.com.mx/lacomer/doHome.action?dep=Sustitutos-de-Leche&key=L%C3%A1cteos-Congelados-y-Huevo&padreId=1139&pasId=21&opcion=listaproductos&path=,1139&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=21&succFmt=100'
                     ]
    pagina_carnes = ['https://www.lacomer.com.mx/lacomer/doHome.action?dep=Cerdo-Selecto&key=Carnes-y-Aves&padreId=1110&pasId=36&opcion=listaproductos&path=,1110&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=36&succFmt=100',
                     'https://www.lacomer.com.mx/lacomer/doHome.action?dep=Pollo-Selecto&key=Carnes-y-Aves&padreId=1119&pasId=36&opcion=listaproductos&path=,1119&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=36&succFmt=100',
                     'https://www.lacomer.com.mx/lacomer/doHome.action?dep=Res-Selecta&key=Carnes-y-Aves&padreId=1128&pasId=36&opcion=listaproductos&path=,1128&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=36&succFmt=100',
                     'https://www.lacomer.com.mx/lacomer/doHome.action?dep=Ternera-selecta&key=Carnes-y-Aves&padreId=1130&pasId=36&opcion=listaproductos&path=,1130&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=36&succFmt=100'
                    ]
    pagina_enlatados = 'https://www.lacomer.com.mx/lacomer/doHome.action?key=Enlatados-y-Conservas&succId=287&padreId=51&pasId=51&opcion=listaproductos&path=,51&pathPadre=0&jsp=PasilloPadre.jsp&noPagina='
    
    '''
    ----------------paginas donde se extrae la informacion de la seccion frutas----------------------
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=287&padreId=14&pasId=13&opcion=listaproductos&path=,14&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=1&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Frutas-
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=287&padreId=14&pasId=13&opcion=listaproductos&path=,14&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=2&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Frutas-
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=287&padreId=14&pasId=13&opcion=listaproductos&path=,14&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=3&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Frutas-
    
    ----------------paginas donde se extrae la informacion de la seccion verduras----------------------    
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=287&padreId=15&pasId=13&opcion=listaproductos&path=,15&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=1&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Verduras
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=287&padreId=15&pasId=13&opcion=listaproductos&path=,15&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=2&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Verduras
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=287&padreId=15&pasId=13&opcion=listaproductos&path=,15&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=3&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Verduras
    
    ----------------paginas donde se extrae la informacion de la seccion lacteos----------------------
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Lácteos-Congelados-y-Huevo&succId=287&padreId=27&pasId=21&opcion=listaproductos&path=,27&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=2&mov=1&subOpc=0&agruId=21&succFmt=100&dep=Bebidas-lácteas-y-Orgánicos
    https://www.lacomer.com.mx/lacomer/doHome.action?dep=Cremas-y-Natas&key=Lácteos-Congelados-y-Huevo&padreId=25&pasId=21&opcion=listaproductos&path=,25&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=21&succFmt=100
    https://www.lacomer.com.mx/lacomer/doHome.action?dep=Huevo-blanco&key=Lácteos-Congelados-y-Huevo&padreId=1188&pasId=21&opcion=listaproductos&path=,1188&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=21&succFmt=100
    
    ----------------paginas donde se extrae la informacion de la seccion carnes----------------------
    https://www.lacomer.com.mx/lacomer/doHome.action?dep=Cerdo-Selecto&key=Carnes-y-Aves&padreId=1110&pasId=36&opcion=listaproductos&path=,1110&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=36&succFmt=100
    https://www.lacomer.com.mx/lacomer/doHome.action?dep=Pollo-Selecto&key=Carnes-y-Aves&padreId=1119&pasId=36&opcion=listaproductos&path=,1119&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=36&succFmt=100
    https://www.lacomer.com.mx/lacomer/doHome.action?dep=Res-Selecta&key=Carnes-y-Aves&padreId=1128&pasId=36&opcion=listaproductos&path=,1128&pathPadre=&mov=1&subOpc=0&jsp=PasilloPadre.jsp&succId=287&agruId=36&succFmt=100
    
    ----------------paginas donde se extrae la informacion de la seccion enlatados----------------------
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Enlatados-y-Conservas&succId=287&padreId=51&pasId=51&opcion=listaproductos&path=,51&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=1&mov=1&subOpc=0&agruId=51&succFmt=100
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Enlatados-y-Conservas&succId=287&padreId=51&pasId=51&opcion=listaproductos&path=,51&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=2&mov=1&subOpc=0&agruId=51&succFmt=100
    https://www.lacomer.com.mx/lacomer/doHome.action?key=Enlatados-y-Conservas&succId=287&padreId=51&pasId=51&opcion=listaproductos&path=,51&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=3&mov=1&subOpc=0&agruId=51&succFmt=100
    '''
    
    paginas = [str(i) for i in range(1,5)] #Se extraen los datos de las primeras 3 paginas 24*5 100 a 120 datos 
    print(paginas)
    
    for tipo_pagina in tipo_paginas:
        #Se realiza un ciclo para cada una de las páginas
        nombres = []
        precios = []
        i = 0
        for pagina in paginas:
            
            #Se realiza una petición según sea el caso
            if tipo_pagina == 0:
                response = get(pagina_frutas + pagina + '&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Frutas-') 
          
            if tipo_pagina == 1:
                response = get(pagina_verduras + pagina + '&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Verduras')
    
            if tipo_pagina == 2:
                response = get(pagina_lacteos[i])
                i+= 1
                
            if tipo_pagina == 3:
                response = get(pagina_carnes[i])
                i+= 1
                
            if tipo_pagina == 4:
                response = get(pagina_enlatados + pagina + '&mov=1&subOpc=0&agruId=51&succFmt=100')
                
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
            if peticiones > 20:
                warn('Number of requests was greater than expected.')
                break
    
            # Parse the content of the request with BeautifulSoup
            html_soup = BeautifulSoup(response.text, 'html.parser')
    
            #Selecciona todos los contenedores de los precios de los productos
            contenedores_productos = html_soup.find_all('div', class_='li_prod_picture')
            
            for contenedor_nombre in contenedores_productos:
                nombres.append(contenedor_nombre.strong.get_text(strip = True))
            
            # Selecciona todos los contenedores de los precios de los productos
            for contenedor_precio in contenedores_productos:
                precios.append(contenedor_precio.find('span', class_ = 'precio_normal').get_text(strip = True)) # .get_text(strip = True) quita los espacios \xa0 al final de la cadena 
                  
        correcion_datos_lacomer(nombres, precios, tipo_pagina) #Se llama a la funcion para corregir los datos obtenidos

def correcion_datos_lacomer(nombres, precios, tipo_pagina):
    
    #Quitando los simbolos $ y convirtiendo en flotante los precios
    i=0
    for precio in precios:
        precios[i] = float((precio.strip('$ M.N')).replace(',',''))
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
        
        nombres_frutas = nombres[:71]
        precios_frutas = precios[:71]
        
        Info_frutas = pd.DataFrame({'Fruta': nombres,
                                      'Precio': precios
                                    })
        print(Info_frutas)
        
        archivo = pd.read_csv("csv/infofrutas.csv") #Se lee el archivo
        archivo['Frutas LaComer'] = nombres_frutas[:60] 
        archivo['Precio Frutas LaComer'] = precios_frutas[:60]
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
        archivo['Verduras LaComer'] = nombres_verduras[:60] 
        archivo['Precio Verduras LaComer'] = precios_verduras[:60]
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
        archivo['Lacteos LaComer'] = nombres_lacteos[:60] 
        archivo['Precio Lacteos LaComer'] = precios_lacteos[:60]
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
        archivo['Carnes LaComer'] = nombres_carnes[:60] 
        archivo['Precio Carnes LaComer'] = precios_carnes[:60]
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
        archivo['Enlatados LaComer'] = nombres_enlatados[:60] 
        archivo['Precio Enlatados LaComer'] = precios_enlatados[:60]
        archivo.to_csv('csv/infoenlatados.csv',encoding = 'utf8',index=False)

        
        info_lacomer = pd.DataFrame({'Frutas':  nombres_frutas,
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
        
        info_lacomer.to_csv('csv/info_lacomer.csv', encoding = 'utf8')

