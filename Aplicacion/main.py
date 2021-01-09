import os # Paquete para las funciones que requieren recursos del OS
import threading
import ActualizaPrecios as ap
import pandas as pd

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRectangleFlatIconButton, MDFlatButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar
######### temp
from time import sleep
from plyer import notification
from random import randint
from kivy.properties import ObjectProperty

# importaciones de archivos py#
from baseclass.settingsscreen import SettingsScreen
from baseclass.utilidades import Banner
from baseclass.sugerenciasscreen import SugerenciasScreen
from baseclass.mapacomercios import MapaComercios
from baseclass.reportegastos import ReporteGastos
from baseclass.inventario import *
from baseclass.listacom import *
from db_inv.db import *

conexion_database(DB_PATH) # crea base de datos de inventario

class DashBoard(Screen):#Pantalla de Convertidor de unidades
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.sub_title = "Convertidor de onzas" 
        
        self.hint_onza_number = "Ingresa la cantidad de onzas"
    
    def on_pre_enter(self, *args):

        """"Funcion que se ejecuta al iniciar la aplicacion, se incluyen diferentes parametros que se desean que apararezcan
        cuando se ejecuta la aplicacion, se cambia el titulo de la aplicacion y se crean las notificaciones iniciales que se
        le mostrarán al usuario"""
        self.app.title = "Convertidor Unidades" #Se cambia el nombre de la pantalla
        self.MuestraNotificacionInicial()


        
    def on_kv_post(self, base_widget): #Se lea el archivo kivy
        grid = self.ids["grid_utilidades"]
        '''
        for i in range(1):
            banner = Banner(title = f'Funcion{i}')
            grid.add_widget(banner)
        '''
        operations ={"onza_gramo": "Onza a Gramos",
                     "gramo_onza": "Gramos a Onzas",
                     "libra_gramo": "Libra a Gramos",
                     "kilogramo_libra": "Kilogramo a Libras",
                     "galon_litro": "Galon a Litro",
                     "litro_galon": "Litro a Galon",
                     "farenheit_celcius": "Farenheit a Celcius",
                     "celcius_farenheit": "Celcius a Farenheit"
                    } 
        
        for operation,title in operations.items():
            banner = Banner(title = title, operation = operation)
            grid.add_widget(banner)
            
            
    def onza_a_gramos(self, cantidad_onzas):
        try:
            gramos = int(cantidad_onzas) * 28.3495
            self.ids["solution"].text = f'Resultado: {gramos} gramos'
            self.ids["solution"].theme_text_color = "Primary"
            
        except ValueError:
            self.ids["solution"].text = "Carácteres no aceptados"
            self.ids["solution"].theme_text_color = "Error"
    pass

    def MuestraNotificacionInicial(self):
        """Muestra la notificacion inicial cuando se inicia la aplicación, esta funcion se llama al inicializar la aplicacion y despliega la notificación"""
        print("Estoy en muestra notifica")

        self.a = randint(1, 5)
        print(self.a)
        if self.a == 1:
            notification.notify(title='Acerca del Convertidor de Unidades',
                                message='Utiliza el convertidor de unidades para transformar rápidamente unidades: '
                                        'Peso: libras, onzas, gramos, kilogramos,'
                                        'Volumen: Litro, Galón,'
                                        'Temperatura: Celsius, Farenheit',
                                timeout=50)
        if self.a == 2:
            notification.notify(title='Acerca de Ajustes',
                                message='Utiliza la sección ajustes para personalizar el aspecto de los menús',
                                timeout=50)

        if self.a == 3:
            notification.notify(title='Acerca del Comparador de precios',
                                message='Utiliza el comparador de precios para encontrar productos como verduras, frutas, carnes, lacteos o enlatados '
                                        'puedes consultar estos precios por tiendas departamentales ',
                                timeout=50)

        if self.a == 4:
            notification.notify(title='Acerca de sugerencias',
                                message='La sección sugerencias puede ser de utilidad para aprender sobre algún aspecto '
                                        'como alimentación o buenos hábitos, ¡no dudes en consultarla!',
                                timeout=50)

        if self.a == 5:
            notification.notify(title='Acerca de mapa de comercios',
                                message='Utiliza el mapa para localizar comercios rápidamente, puedes localizar con un solo click la ubicacion de '
                                        'HEB, Chedraui, La Comer y Soriana',
                                timeout=50)

        pass


class FirstScreen(Screen): #Pantalla comparador de precios
    """Clase principal donde se ejecuta el modulo comparador de precios, en ella se inicializan las variables correspondientes que se
    utilizaran en el módulo"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.valorbarra = 0

        self.buttonactualizar = MDRectangleFlatIconButton(
                                       pos_hint = {"center_x":.5, "top": .95},
                                       #size_hint = (.3,.1),
                                       icon = "cart-arrow-down",
                                       text = " Precios",
                                       )
        self.msgactualiza = MDLabel(text = 'Actualizando, espera por favor',
                                    pos_hint = {"center_x": .5, "top":.87},
                                    size_hint = (.8,.1),
                                    theme_text_color = "Primary",
                                    font_style= "Subtitle1",
                                    halign = "center"
                                    )

        self.barra = MDProgressBar(id= "barrasss",
                                   value=0,
                                   pos_hint={"center_x": .5, "center_y": .80},
                                   size_hint= (.9,.1)
                                   )

        self.etiqueta1 = MDLabel(text = 'Consultar por Tienda',
                             pos_hint = {"center_x": .5, "top":.80},
                             size_hint = (.5,.1),
                             theme_text_color = "Primary", 
                             font_style= "Subtitle1",
                             halign = "center")
        
        self.buttonche = MDFillRoundFlatButton(
                pos_hint = {"x": .05, "y": .6},
                size_hint = (.40,.1),
                text = "Chedraui",
                on_release = lambda x: self.verboton('che')
                )        
        
        self.buttonsor = MDFillRoundFlatButton(
                pos_hint = {"x": .55, "y": .6},
                size_hint = (.40,.1),
                text = "Soriana",
                on_release = lambda x: self.verboton('sor')
                )
        
        self.buttonhbe = MDFillRoundFlatButton(
                pos_hint = {"x": .05, "y": .45},
                size_hint = (.40,.1),
                #theme_text_color = "Primary",
                text = "HBE",
                on_release = lambda x: self.verboton('hbe')
                )
        
        self.buttoncomer = MDFillRoundFlatButton(
                pos_hint = {"x": .55, "y": .45},
                size_hint = (.40,.1),
                text = "La Comer",
                on_release = lambda x: self.verboton('comer')
                )
        
        self.etiqueta2 = MDLabel(text = 'Consultar por Categoría',
                             pos_hint = {"center_x": .5, "top":.40},
                             size_hint = (.5,.1),
                             theme_text_color = "Primary", 
                             font_style= "Subtitle1",
                             halign = "center")
        
        self.buttonfrutas = MDFillRoundFlatButton(
                                       pos_hint = {"x":.05, "y": .20},
                                       size_hint = (.25,.1),
                                       text = "Frutas",
                                       on_release = lambda x: self.verboton('frutas'))
        
        self.buttonverduras = MDFillRoundFlatButton(
                                       pos_hint = {"x":.35, "y": .20},
                                       size_hint = (.25,.1),
                                       text = "Verduras",
                                       on_release = lambda x: self.verboton('verduras')
                                       )
        
        self.buttoncarnes = MDFillRoundFlatButton(
                                       pos_hint = {"x":.65, "y": .20},
                                       size_hint = (.25,.1),
                                       text = 'Carnes',
                                       on_release = lambda x: self.verboton('carnes')
                                       )
        
        self.buttonlacteos = MDFillRoundFlatButton(
                                       pos_hint = {"x":.20, "y": .05},
                                       size_hint = (.25,.1),
                                       text = 'Lácteos',
                                       on_release = lambda x: self.verboton('lacteos')
                                       )
        
        self.buttonenlatados = MDFillRoundFlatButton(
                                       pos_hint = {"x":.50, "y": .05},
                                       size_hint = (.25,.1),
                                       text = 'Enlatados',
                                       on_release = lambda x: self.verboton('enlatados')
                                       )

        self.buttonactualizar.bind(on_press=lambda x: self.ActualizaPrecio())

        self.add_widget(self.buttonactualizar)

        self.add_widget(self.buttonche)
        self.add_widget(self.buttonsor)
        self.add_widget(self.buttonhbe)
        self.add_widget(self.buttoncomer)
        self.add_widget(self.etiqueta1)
        self.add_widget(self.etiqueta2)
        self.add_widget(self.buttonfrutas)
        self.add_widget(self.buttonverduras)
        self.add_widget(self.buttoncarnes)
        self.add_widget(self.buttonlacteos)
        self.add_widget(self.buttonenlatados)

        #food-steak carne food-drumstick
        #food-apple fruta
        #cheese lacteos
        #carrot verduras
        #dome-light
        #return self.button
    #def tabla(self, widget):

    def MuestraNotificacionComparador(self):
        """Se muestra las notificaciones que se anexaron al modulo del comparador de precios"""
        self.a = randint(1, 5)
        print(self.a)
        if self.a == 1:

            notification.notify(title='Como Actualizar los precios',
                                message='Puedes actualizar los precios de los productos pulsando el boton de Actualizar que se encuentra en'
                                        'la parte superior',
                                timeout=20)

        if self.a == 2:
            notification.notify(title='Visualización de los Precios',
                                message='Los precios pueden ser consultados deslizando la tabla que se muestra al consultar alguna categoría',
                                timeout=20)

        pass

    def ActualizaPrecio(self):
        """Función desde la cual se obtienen los precios, se llama una funcion que esta en el fichero Actualiza Precios, se ejecutan hilos
        para obtener los precios simultaneamente, de esta manera se previene el congelamiento de la aplicación, en esta función tambien se
        llama a la funcion actualiza barra"""
        ap.main()

        self.add_widget(self.barra)
        self.add_widget(self.msgactualiza)
        self.buttonactualizar.disabled = True
        self.hiloactualiza = threading.Thread(target=self.actualizabarra)  # Inicializar un hilo llamando a una funcion
        self.hiloactualiza.start()


        #self.actualizabarra()


        self.dialog = MDDialog(title = "Actualización de Precios",
                               text = "Se actualizarán los precios que se muestran en cada una de las categorías del comparador de precios,"
                                      " este proceso puede demorar algunos  un par de minutos, por favor sea paciente",
                               size_hint=[.9, .9],
                               auto_dismiss=True,

                               buttons=[MDFlatButton(
                                   text="CERRAR",
                                   on_release=self.dialog_close),
                               ]
                               )
        self.dialog.open()
    def actualizabarra(self):
        """Funcion que actualiza la barra mostrada en el módulo comparador de precios"""
        #if ap.sor.correccion_datos_sor() == True:
        for a in range(100):
            self.valorbarra = self.valorbarra + 1
            self.barra.value= self.valorbarra
            sleep(1.3)

        sleep(5)
        self.remove_widget(self.msgactualiza)
        sleep(1)
        self.remove_widget(self.barra)



    def dialog_close(self, *args): # Cierra el dialog del boton ayuda
        """Funcion que cierra el dialog que se despliega al oprimir el botón actualizar"""
        print("Cerrando Dialog")
        self.dialog.dismiss()
        
    def verboton(self, valor):
        self.MuestraNotificacionComparador()
        if valor == 'comer':
            datos = pd.read_csv("csv/info_lacomer.csv", encoding = 'utf8')
        elif valor == 'hbe':
            datos = pd.read_csv("csv/info_hbe.csv", encoding = 'utf8')
        elif valor == 'sor':
            datos = pd.read_csv("csv/info_sor.csv", encoding = 'utf8')
        elif valor == 'che':
            datos = pd.read_csv("csv/info_che.csv", encoding = 'utf8')
        elif valor == 'frutas':
            datos = pd.read_csv("csv/infofrutas.csv", encoding = 'utf8')
        elif valor == 'verduras':
            datos = pd.read_csv("csv/infoverduras.csv", encoding = 'utf8')
        elif valor == 'carnes':
            datos = pd.read_csv("csv/infocarnes.csv", encoding = 'utf8')
        elif valor == 'lacteos':
            datos = pd.read_csv("csv/infolacteos.csv", encoding = 'utf8')
        elif valor == 'enlatados':
            datos = pd.read_csv("csv/infoenlatados.csv", encoding = 'utf8')
        
        datos = datos.iloc[:,1: ]# primer arg selecciona todas las filas, segundo 
        cols = datos.columns.values
        values = datos.values
        
        self.table = MDDataTable(pos_hint={'center_x':0.5, 'center_y':0.5 },
                            size_hint=(0.99, 0.99),
                            #font_size = 10,
                            #check= True,
                            use_pagination= True,
                            rows_num=10,
                            column_data =[
                                    (col, dp(40))
                                    for col in cols
                                         ],
                            row_data= values)
        
        self.table.bind(on_check_press=self.check_press)
        self.table.bind(on_check_press=self.row_press)

        self.table.open()
        print(valor)

    def my_callback(self, texto, popup_widget): # funcion que ayuda a cerrar el dialog del boton actualizar
        print(texto)
        print(popup_widget)

    def open_table(self, instance):
        """Despliega el contenido de la tabla correpondiente al boton pulsado"""
        #screen.add_widget(table)
        self.table.open()
        
    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)
        
    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)
        #self.sub_title = "Comparador" 
    
    def on_pre_enter(self, *args):
        self.app.title = "Comparador de precios"
    pass
        
class MyApp(MDApp):
    el_idca = ObjectProperty()  # variable global para guardar id de categoria
    def build(self):
        self.title = "Inventario" #Titulo de la aplicación
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('main.kv')
MyApp().run()