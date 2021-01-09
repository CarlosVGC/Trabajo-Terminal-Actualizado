from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from datetime import datetime

from plyer import notification
from random import randint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        
    def on_pre_enter(self, *args):
        self.app.title = "Ajustes"
        self.MuestraNotificacionInicial()

    def MuestraNotificacionInicial(self):
        """Muestra la notificacion inicial cuando se inicia la aplicación, esta funcion se llama al inicializar la aplicacion y despliega la notificación"""
        print("Estoy en muestra notifica")

        self.a = randint(1, 2)#
        print(self.a)
        if self.a == 1:
            notification.notify(title='Puedes personalizar el esquema de colores',
                                message='Selecciona el esquema de tu preferencia en la sección de ajuste, busca el simbolo de una brocha, ese es el lugar',
                                timeout=20)
        if self.a == 2:
            notification.notify(title='Cambia a modo nocturno',
                                message='Si deseas cambiar a modo nocturno puedes hacerlo en la parte de ajustes,en  la primera opción que se muestra puedes hacerlo',
                                timeout=20)
        
    def cambiar_modo(self, checkbox, value):
        if value:
            self.app.theme_cls.theme_style = "Dark"
            
        else:
            self.app.theme_cls.theme_style = "Light"
            
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

        #tema = theme_dialog
        print(theme_dialog.background_hue)

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
                archivo.GetContentFile('database.db')  # Download file as 'catlove.png'.

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