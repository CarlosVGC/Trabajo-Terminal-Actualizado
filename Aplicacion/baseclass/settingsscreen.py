from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from datetime import datetime

from plyer import notification
from random import randint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from kivy.uix.image import Image

from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDRaisedButton



class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

        self.esqcolores = Image(source="imagenes/Colores2.png",
                        pos_hint={"x": .248, "y": .60},
                        size_hint = (0.70, None))

        self.boton1 = MDRectangleFlatButton(
            pos_hint = {"x": .1, "top": .80},
            text = '1',
            size_hint= (.05, .05),
            text_color = (244/255, 67/255, 54/255, 1),
            on_release=lambda x: self.tema('Red')
        )

        self.boton2 = MDRectangleFlatButton(
            pos_hint={"x": .16, "top": .80},
            text='2',
            size_hint=(.05, .05),
            text_color = (233/255, 30/255, 99/255, 1),
            on_release=lambda x: self.tema('Pink')

        )

        self.boton3 = MDRectangleFlatButton(
            pos_hint={"x": .22, "top": .80},
            text='3',
            size_hint=(.05, .05),
            text_color=(156 / 255, 39 / 255, 176 / 255, 1),
            on_release=lambda x: self.tema('Purple')
        )

        self.boton4 = MDRectangleFlatButton(
            pos_hint={"x": .28, "top": .80},
            text='4',
            size_hint=(.05, .05),
            text_color=(103/255, 58/255, 183/255, 1),
            on_release=lambda x: self.tema('DeepPurple')
        )

        self.boton5 = MDRectangleFlatButton(
            pos_hint={"x": .34, "top": .80},
            text='5',
            size_hint=(.05, .05),
            text_color=(63/255, 81/255, 181/255, 1),
            on_release = lambda x: self.tema('Indigo')
        )

        self.boton6 = MDRectangleFlatButton(
            pos_hint={"x": .1, "top": .74},
            text='6',
            size_hint=(.05, .05),
            text_color=(33/255, 150/255, 243/255, 1),
            on_release=lambda x: self.tema('Blue')
        )

        self.boton7 = MDRectangleFlatButton(
            pos_hint={"x": .16, "top": .74},
            text='7',
            size_hint=(.05, .05),
            text_color=(3/255, 169/255, 244/255, 1),
            on_release = lambda x: self.tema('LightBlue')
        )

        self.boton8 = MDRectangleFlatButton(
            pos_hint={"x": .22, "top": .74},
            text='8',
            size_hint=(.05, .05),
            text_color=(0/ 255, 188/ 255, 212/ 255, 1),
            on_release = lambda x: self.tema('Cyan')
        )

        self.boton9 = MDRectangleFlatButton(
            pos_hint={"x": .28, "top": .74},
            text='9',
            size_hint=(.05, .05),
            text_color=(0/ 255, 150/ 255, 136/ 255, 1),
            on_release=lambda x: self.tema('Teal')
        )

        self.boton10 = MDRectangleFlatButton(
            pos_hint={"x": .34, "top": .74},
            text='10',
            size_hint=(.05, .05),
            text_color=(76/ 255, 175/ 255, 80/ 255, 1),
            on_release=lambda x: self.tema('Green')
        )

        self.boton11 = MDRectangleFlatButton(
            pos_hint={"x": .1, "top": .68},
            text='11',
            size_hint=(.05, .05),
            text_color=(139/ 255, 195/ 255, 74/ 255, 1),
            on_release = lambda x: self.tema('LightGreen')
        )

        self.boton12 = MDRectangleFlatButton(
            pos_hint={"x": .16, "top": .68},
            text='12',
            size_hint=(.05, .05),
            text_color=(205/ 255, 220/ 255, 57/ 255, 1),
            on_release=lambda x: self.tema('Lime')
        )

        self.boton13 = MDRectangleFlatButton(
            pos_hint={"x": .22, "top": .68},
            text='13',
            size_hint=(.05, .05),
            text_color=(255/ 255, 235/ 255, 59/ 255, 1),
            on_release=lambda x: self.tema('Yellow')
        )

        self.boton14 = MDRectangleFlatButton(
            pos_hint={"x": .28, "top": .68},
            text='14',
            size_hint=(.05, .05),
            text_color=(255/ 255, 193/ 255, 7/ 255, 1),
            on_release=lambda x: self.tema('Amber')
        )

        self.boton15 = MDRectangleFlatButton(
            pos_hint={"x": .34, "top": .68},
            text='15',
            size_hint=(.05, .05),
            text_color=(255/ 255, 152/ 255, 0/ 255, 1),
            on_release=lambda x: self.tema('Orange')
        )

        self.boton16 = MDRectangleFlatButton(
            pos_hint={"x": .1, "top": .62},
            text='16',
            size_hint=(.05, .05),
            text_color=(255/ 255, 87/ 255, 34/ 255, 1),
            on_release=lambda x: self.tema('DeepOrange')
        )

        self.boton17 = MDRectangleFlatButton(
            pos_hint={"x": .16, "top": .62},
            text='17',
            size_hint=(.05, .05),
            text_color=(121/ 255, 85/ 255, 72/ 255, 1),
            on_release=lambda x: self.tema('Brown')
        )

        self.boton18 = MDRectangleFlatButton(
            pos_hint={"x": .22, "top": .62},
            text='18',
            size_hint=(.05, .05),
            text_color=(158/ 255, 158/ 255, 158/ 255, 1),
            on_release=lambda x: self.tema('Gray')
        )

        self.boton19 = MDRectangleFlatButton(
            pos_hint={"x": .28, "top": .62},
            text='19',
            size_hint=(.05, .05),
            text_color=(96/ 255, 125/ 255, 139/ 255, 1),
            on_release=lambda x: self.tema('BlueGray'))

        self.botonobscuro = MDRectangleFlatButton(
            pos_hint={"x": .35, "top": .96},
            text='Activar',
            size_hint=(.15, .05),
            text_color=(48/ 255, 48/ 255, 48/ 255, 1),
            on_release=lambda x: self.cambiar_modo('obscuro'))

        self.botonclaro = MDRectangleFlatButton(
            pos_hint={"x": .55, "top": .96},
            text='Desactivar',
            size_hint=(.15, .05),
            text_color=(192 / 192, 255 / 255, 192 / 255, 1),
            on_release=lambda x: self.cambiar_modo('claro'))

        self.botonopabaja=MDRectangleFlatButton(
            pos_hint={"x": .8, "top": .80},
            text='Baja',
            size_hint=(.10, .05),
            text_color=(0/ 255, 0/ 255, 0/ 255, 1),
            on_release=lambda x: self.opacidad('Baja'))

        self.botonopamedia = MDRectangleFlatButton(
            pos_hint={"x": .8, "top": .70},
            text='Media',
            size_hint=(.10, .05),
            text_color=(0 / 255, 0 / 255, 0 / 255, 1),
            on_release=lambda x: self.opacidad('Media'))

        self.botonopaalta = MDRectangleFlatButton(
            pos_hint={"x": .8, "top": .60},
            text='Alta',
            size_hint=(.10, .05),
            text_color=(0 / 255, 0 / 255, 0 / 255, 1),
            on_release=lambda x: self.opacidad('Alta'))



        #self.boton1.bind(on_press=lambda x: self.tema())

        self.add_widget(self.esqcolores)

        self.add_widget(self.boton1)
        self.add_widget(self.boton2)
        self.add_widget(self.boton3)
        self.add_widget(self.boton4)
        self.add_widget(self.boton5)
        self.add_widget(self.boton6)
        self.add_widget(self.boton7)
        self.add_widget(self.boton8)
        self.add_widget(self.boton9)
        self.add_widget(self.boton10)
        self.add_widget(self.boton11)
        self.add_widget(self.boton12)
        self.add_widget(self.boton13)
        self.add_widget(self.boton14)
        self.add_widget(self.boton15)
        self.add_widget(self.boton16)
        self.add_widget(self.boton17)
        self.add_widget(self.boton18)
        self.add_widget(self.boton19)

        self.add_widget(self.botonopabaja)
        self.add_widget(self.botonopamedia)
        self.add_widget(self.botonopaalta)

        self.add_widget(self.botonclaro)
        self.add_widget(self.botonobscuro)
        
    def on_pre_enter(self, *args):
        self.app.title = "Ajustes"
        self.MuestraNotificacionInicial()
        #self.ids["mode"] = False

    def MuestraNotificacionInicial(self):
        """Muestra la notificacion inicial cuando se inicia la aplicación, esta funcion se llama al inicializar la aplicacion y despliega la notificación"""
        print("Estoy en muestra notifica")

        self.a = randint(1, 6)#
        print(self.a)
        if self.a == 1:
            notification.notify(title='Puedes personalizar el esquema de colores',
                                message='Selecciona el esquema de tu preferencia en la sección de ajuste, busca el simbolo de una brocha, ese es el lugar',
                                timeout=20)
        if self.a == 2:
            notification.notify(title='Cambia a modo nocturno',
                                message='Si deseas cambiar a modo nocturno puedes hacerlo en la parte de ajustes,en  la primera opción que se muestra puedes hacerlo',
                                timeout=20)
        
    def cambiar_modo(self, valor):
        modo = ''
        if valor == 'obscuro':
            modo = 'Dark'
            self.app.theme_cls.theme_style = "Dark"

        elif valor == 'claro':
            modo = 'Light'
            self.app.theme_cls.theme_style = "Light"

        a_file = open("conf.txt", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[1] = modo + "\n"

        a_file = open("conf.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

        #print("tema")
        #print(self.app.theme_cls.theme_style)
        print(valor)

    def tema(self, color):
        #self.app.theme_cls.theme_style = "Orange"
        colores = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
                   'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
          # "Purple", "Red"
        #self.app.theme_cls.primary_hue = "200"  # "500"

        if color == 'Red':
            self.app.theme_cls.primary_palette = "Red"
        elif color == 'Pink':
            self.app.theme_cls.primary_palette = "Pink"
        elif color == 'Purple':
            self.app.theme_cls.primary_palette = "Purple"
        elif color == 'DeepPurple':
            self.app.theme_cls.primary_palette = "DeepPurple"
        elif color == 'Indigo':
            self.app.theme_cls.primary_palette = "Indigo"
        elif color == 'Blue':
            self.app.theme_cls.primary_palette = "Blue"
        elif color == 'LightBlue':
            self.app.theme_cls.primary_palette = "LightBlue"
        elif color == 'Cyan':
            self.app.theme_cls.primary_palette = "Cyan"
        elif color == 'Teal':
            self.app.theme_cls.primary_palette = "Teal"
        elif color == 'Green':
            self.app.theme_cls.primary_palette = "Green"
        elif color == 'LightGreen':
            self.app.theme_cls.primary_palette = "LightGreen"
        elif color == 'Lime':
            self.app.theme_cls.primary_palette = "Lime"
        elif color == 'Yellow':
            self.app.theme_cls.primary_palette = "Yellow"
        elif color == 'Amber':
            self.app.theme_cls.primary_palette = "Amber"
        elif color == 'Orange':
            self.app.theme_cls.primary_palette = "Orange"
        elif color == 'DeepOrange':
            self.app.theme_cls.primary_palette = "DeepOrange"
        elif color == 'Brown':
            self.app.theme_cls.primary_palette = "Brown"
        elif color == 'Gray':
            self.app.theme_cls.primary_palette = "Gray"
        elif color == 'BlueGray':
            self.app.theme_cls.primary_palette = "BlueGray"

        a_file = open("conf.txt", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[0] = color + "\n"

        a_file = open("conf.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

        print(color)

    def opacidad(self,opacidad):
        print(opacidad)
        if opacidad == 'Baja':
            self.app.theme_cls.primary_hue = "200"  # "500"
        elif opacidad == 'Media':
            self.app.theme_cls.primary_hue = "500"  # "500"
        elif opacidad == 'Alta':
            self.app.theme_cls.primary_hue = "900"  # "500"

        a_file = open("conf.txt", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[2] = opacidad + "\n"

        a_file = open("conf.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()


            
    def get_date(self, date): #tiempo
        '''
        :type date: <class 'datetime.date'>
        '''
        
        self.ids["fecha"].text = date.strftime("%d/%m/%Y") #se le cambia el formato a la fecha
    
    def get_time(self, instance, time):
        '''
        The method returns the set time
        
        :type instance <kivy.uix.picker.MDtimePicker object>
        :type time: <class 'datetime.time'>
        '''
        self.ids["hora"].text = time.strftime("%H:%M") #el id hora (a etiqueta) mostrará la hora que se selecciono
    

    def show_date_picker(self): #funcion con la cual se utiliza el picker de tiempo
        #min_date = datetime.strptime("01:10:2020", "%d:%m:%Y").date()
        #ax_date = datetime.strptime("01:10:2020", "%d:%m:%Y").date()
        date_dialog = MDDatePicker(callback = self.get_date)
        date_dialog.open()
        
    def show_time_picker(self): #funcion con la cual se utiliza el picker de hora
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()
        
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()


    def subir_archivo(self):
        print("Subiendo")

        gauth = GoogleAuth()
        # Try to load saved client credentials
        gauth.LoadCredentialsFile("mycreds.txt")
        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
        # Save the current credentials to a file
        gauth.SaveCredentialsFile("mycreds.txt")

        drive = GoogleDrive(gauth)

        folderName = "App Inventario"
        # folder = drive.CreateFile({'title' : folderName, 'mimeType' : 'application/vnd.google-apps.folder'})
        # folder.Upload()

        fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        contador = 0

        if len(fileList) == 0:  # No hay archivos
            print("No hay ningun archivo, creando el folder")
            folder = drive.CreateFile({'title': folderName, 'mimeType': 'application/vnd.google-apps.folder'})
            folder.Upload()
            contador = -1

        for file in fileList:  # haciendo un for para comprobar los archivos
            # print('Title: %s, ID: %s' % (file['title'], file['id']))
            # Get the folder ID that you want
            if file['title'] == folderName:
                print("Existe el folder necesario")
                contador = -1
                break
            elif file['title'] != folderName:
                print("Archivo sin coincidencia")
                print('Title: %s, ID: %s' % (file['title'], file['id']))
                contador = contador + 1

        if contador == len(fileList):  # si son iguales significa que no existe carpeta de la App
            print("Se debe crear el archivo")
            folder = drive.CreateFile({'title': folderName, 'mimeType': 'application/vnd.google-apps.folder'})
            folder.Upload()

        # -------Parte de actualizar arc

        folderName = "App Inventario"
        folder_id = ''
        # creacion archivo en un folder específico
        # folders = drive.ListFile(
        # {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()

        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

        for file in file_list:
            if (file['title'] == folderName):
                folder_id = file['id']

                break

        # 3) Build string dynamically (need to use escape characters to support single quote syntax)
        str = "\'" + folder_id + "\'" + " in parents and trashed=false"

        # 4) Starting iterating over files
        file_list = drive.ListFile({'q': str}).GetList()
        for file in file_list:
            print('title: %s, id: %s' % (file['title'], file['id']))
            if file['title'] == "database.db":
                file.Delete()
        file2 = drive.CreateFile({'parents': [{'id': folder_id}]})
        file2.SetContentFile('database.db')
        file2.Upload()

        #Informar que se ha subido
        snackbar = Snackbar(text="Se ha realizado el respaldo")
        snackbar.show()

    def descargar_archivo(self):
        print("descargando")

        gauth = GoogleAuth()
        # Try to load saved client credentials
        gauth.LoadCredentialsFile("mycreds.txt")
        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
        # Save the current credentials to a file
        gauth.SaveCredentialsFile("mycreds.txt")

        drive = GoogleDrive(gauth)


        folderName = "App Inventario"
        folder_id = ''
        # creacion archivo en un folder específico
        # folders = drive.ListFile(
        #    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()

        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

        for file in file_list:
            if (file['title'] == folderName):
                folder_id = file['id']

                break

        # 3) Build string dynamically (need to use escape characters to support single quote syntax)
        str = "\'" + folder_id + "\'" + " in parents and trashed=false"

        # 4) Starting iterating over files
        file_list = drive.ListFile({'q': str}).GetList()

        for file in file_list:
            print('title: %s, id: %s' % (file['title'], file['id']))
            if file['title'] == "database.db":
                archivo = drive.CreateFile({'id': file['id']})
                archivo.GetContentFile('database.db')  # Download file as 'database.db'.

        # Informar que se ha descargado el archivo
        snackbar = Snackbar(text="Se ha recuperado el inventario")
        snackbar.show()

    def borrar_archivo(self):
        print("borrando")

        gauth = GoogleAuth()
        # Try to load saved client credentials
        gauth.LoadCredentialsFile("mycreds.txt")
        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
        # Save the current credentials to a file
        gauth.SaveCredentialsFile("mycreds.txt")

        drive = GoogleDrive(gauth)

        folderName = "App Inventario"
        folder_id = ''
        # creacion archivo en un folder específico
        folders = drive.ListFile(
            {
                'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()

        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

        for file in file_list:
            if (file['title'] == folderName):
                folder_id = file['id']

                break

        # 3) Build string dynamically (need to use escape characters to support single quote syntax)
        str = "\'" + folder_id + "\'" + " in parents and trashed=false"

        # 4) Starting iterating over files
        file_list = drive.ListFile({'q': str}).GetList()
        for file in file_list:
            print('title: %s, id: %s' % (file['title'], file['id']))
            if file['title'] == "ReporteGastos.pdf":
                file.Delete()
            if file['title'] == "database.db":
                file.Delete()

        # Informar que se ha borrado el archivo
        snackbar = Snackbar(text="Los datos contenidos en Google Drive han sido borrados")
        snackbar.show()

"""
Codigo que se podria utilizar posteriormente
        
         MDLabel:
            id: hora
            pos_hint: {"x": .4,"top": .5 }
            size_hint: (.5,.1)
            text: "Hora a mostrar notificaciones"
            
        MDIconButton:
            pos_hint: {"x": .15,"top": .5 }
            size_hint: (.2, .1)
            icon: "clock"
            on_release: root.show_time_picker()

        MDIconButton:
            pos_hint: {"x": .15,"top": .7 }
            size_hint: (.2, .1)
            icon: "format-paint"
            on_release: root.show_theme_picker()

        MDLabel:
            id: temas
            pos_hint: {"x": .4,"top": .7 }
            size_hint: (.5,.1)
            text: "Seleccione un tema"
            
        MDIconButton:
            pos_hint: {"x": .15,"top": .6 }
            size_hint: (.2, .1)
            icon: "calendar"
            on_release: root.show_date_picker()
            
        MDLabel:
            id: fecha
            pos_hint: {"x": .4,"top": .6 }
            size_hint: (.5,.1)
            text: "Seleccione una fecha"
            
        MDSwitch:
            id: mode
            pos_hint: {"x":.7,"top": .99 }
            size_hint: (.2, .1)
            on_active: root.cambiar_modo(*args)
"""