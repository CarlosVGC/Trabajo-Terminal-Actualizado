import os
import kivymd
import datetime
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.popup import Popup
import numpy as np
import speech_recognition as sr


from db_inv.db import * #para conectarnos a la db

class Inventario(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH+'/database.db'

# instancia para widget de las categorias
        self.CategoriasWid = CategoriasWid(self)
        wid = Screen(name='categorias_w')
        wid.add_widget(self.CategoriasWid)
        self.add_widget(wid)
    # instancia y widget para insertar categorias
        self.InsertCatWid = BoxLayout()
        wid = Screen (name='insertCat')
        wid.add_widget(self.InsertCatWid)
        self.add_widget(wid)
    # instancia y widget para actualizar categorias
        self.UpdateDataCateWid = BoxLayout()
        wid = Screen(name='updatedataCate')
        wid.add_widget(self.UpdateDataCateWid)
        self.add_widget(wid)
# instancia para widget de las categorias
        self.ProductosWid = ProductosWid(self)
        wid = Screen(name='producto_w')
        #self.remove_widget(self.ProductosWid)
        self.add_widget(self.ProductosWid)
        self.add_widget(wid)
    # instancia y widget para insertar producto
        self.InsertProWid = BoxLayout()
        wid2 = Screen (name ='insertPro')
        wid2.add_widget(self.InsertProWid)
        self.add_widget(wid2)
    #instancia y widget para actualizar productos
        self.UpdateProyeWid = BoxLayout()
        wid2 = Screen (name ='updatedataProd')
        wid2.add_widget(self.UpdateProyeWid)
        self.add_widget(wid2)

        self.arranca()

    def arranca(self):
        self.remove_widget(self.ProductosWid)
        self.CategoriasWid.check_memory_cat()
        self.current = 'categorias_w'

    def goto_insertCat(self):
        self.InsertCatWid.clear_widgets()
        wid = InsertCatWid(self)
        self.InsertCatWid.add_widget(wid)
        self.current = 'insertCat'

    def cerrar_insertCat(self):
        print('cerrar insertar categorias')
        self.InsertCatWid.clear_widgets()
        self.CategoriasWid.check_memory_cat()
        self.current = 'categorias_w'

    def goto_updatedataCate(self, dataCat_id):
        self.UpdateDataCateWid.clear_widgets()
        wid = UpdateDataCateWid(self, dataCat_id)
        self.UpdateDataCateWid.add_widget(wid)
        self.current = 'updatedataCate'

    def cerrar_updateCat(self):
        self.UpdateDataCateWid.clear_widgets()
        self.CategoriasWid.check_memory_cat()
        self.current = 'categorias_w'

#widget de Productos...
    def goto_producto_w(self):
        self.ProductosWid.check_memory_pro()
        self.add_widget(self.ProductosWid)
        self.current = 'producto_w'

    #funcion que hace volver a categorias_w
    def volveracatego_w(self):
        #self.ProductosWid.clear_widgets()
        self.remove_widget(self.ProductosWid)
        self.CategoriasWid.check_memory_cat()
        self.current = 'categorias_w'

    def goto_insertPro(self):
        self.InsertProWid.clear_widgets()
        self.remove_widget(self.ProductosWid)
        wid = InsertProWid(self)
        self.InsertProWid.add_widget(wid)
        self.current = 'insertPro'

    def cerrar_insertPro(self):
        print('cerrar insertar Productos')

        self.InsertProWid.clear_widgets()
        # self.ProductosWid.check_memory_pro()
        #
        # self.current = 'producto_w'
        self.goto_producto_w()

    def goto_updatedataProd(self, dataPro_id):
        self.UpdateProyeWid.clear_widgets()
        self.remove_widget(self.ProductosWid)
        wid = UpdateProyeWid(self, dataPro_id)
        self.UpdateProyeWid.add_widget(wid)
        self.current='updatedataProd'

    def cerrar_updatePro(self):
        print('cerrar insertar Productos')
        # self.remove_widget(self.UpdateProyeWid)
        # self.UpdateProyeWid.clear_widgets()
        self.UpdateProyeWid.clear_widgets()
        self.goto_producto_w()

##Definicion que cambia nombre de tool
    def on_pre_enter(self, **args):
        self.app.title = "Inventario"

class DataWid_Cat(BoxLayout):
    def __init__(self, mainapp, **kwargs):
        super(DataWid_Cat, self).__init__()
        self.mainapp = mainapp

    def update_data_Cat(self,dataCat_id):
        self.mainapp.goto_updatedataCate(dataCat_id)

    def database_produ(self):
        print ('este es el dataCat_id' + self.dataCat_id)
        self.mainapp.goto_producto_w()

class CategoriasWid(BoxLayout):
    def __init__(self, mainapp, **kwargs):
        super(CategoriasWid, self).__init__()
        self.mainapp = mainapp

    def check_memory_cat(self):
        self.ids.container.clear_widgets()
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        cursor.execute(''' SELECT id, nombre FROM CATEGORIAS ''')
        for i in cursor:
            wid = DataWid_Cat(self.mainapp)
            r1 = 'ID Categoria:' + str(100000 + i[0])[1:9] + '\n'
            r2 = i[1] + '\n'
            wid.dataCat_id = str(i[0])
            wid.dataCat = r1 + r2
            self.ids.container.add_widget(wid)
        wid = NuevoCatButton(self.mainapp)
        self.ids.container.add_widget(wid)
        connection.close()

class InsertCatWid(BoxLayout):
    def __init__(self,mainapp,**kwargs):
        super(InsertCatWid, self).__init__()
        self.mainapp = mainapp
        hoy = datetime.date.today()
        print(hoy)
        self.ids.insertarcategoria_Fecha.text = str(hoy)

    def insertcat(self):
        #insertarcategoria(self)
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        d1 = self.ids.insertarcategoria_Nombre.text
        d2 = self.ids.insertarcategoria_Descripcion.text
        d3 = self.ids.insertarcategoria_Fecha.text
        a1 = (d1, d2, d3)
        s1 = 'INSERT INTO CATEGORIAS(nombre, descripcion, fechacat)'
        s2 = 'VALUES ("%s", "%s", "%s")' % a1
        try:
            cursor.execute(s1 + '' + s2)
            connection.commit()
            connection.close()
            self.mainapp.cerrar_insertCat()
            #print("categoria agregada")

        except Exception as e:
            print('error')
            connection.close()

    def back_to_dbw(self):
        self.mainapp.cerrar_insertCat()
#### se agrega def para voz
    def voz_boton(self, texto):
        r = sr.Recognizer()
        print(texto)
        try:
            with sr.Microphone() as source:
                #r.adjust_for_ambient_noise(source)
                #print("Hable ahora...")
                audio = r.listen(source)
                entrada = r.recognize_google(audio, language='es-ES')
                if (texto=='NombreC'):
                    self.ids.insertarcategoria_Nombre.text = entrada
                elif(texto=='DescripC'):
                    self.ids.insertarcategoria_Descripcion.text = entrada

        except NotImplementedError:
            popup = Popup()
            popup.open()
        except :
            print("no entendi o tardo demasiado")

class NuevoCatButton(MDRaisedButton):
    def __init__(self, mainapp, **kwargs):
        super(NuevoCatButton, self).__init__()
        self.mainapp = mainapp

    def create_new_categoria(self):
        self.mainapp.goto_insertCat()

class UpdateDataCateWid(BoxLayout):
    def __init__(self, mainapp, dataCat_id,**kwargs):
        super(UpdateDataCateWid, self).__init__()
        self.mainapp = mainapp
        self.dataCat_id = dataCat_id
        self.check_memory_cat()

    def check_memory_cat(self):
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        s = 'SELECT nombre, descripcion FROM CATEGORIAS WHERE id='
        cursor.execute(s + self.dataCat_id)
        for i in cursor:
            self.ids.insertarcategoria_Nombre.text = i[0]
            self.ids.insertarcategoria_Descripcion.text = str(i[1])
            #self.ids.Descripcion.text = i[1]
            # self.ids.in_idUser = str(i[1])
        connection.close()

    def update_data_Cat(self):
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        d1 = self.ids.insertarcategoria_Nombre.text
        d2 = self.ids.insertarcategoria_Descripcion.text
        a1 = (d1, d2)
        s1 = 'UPDATE CATEGORIAS SET'
        s2 = ' nombre="%s" , descripcion = "%s" ' % a1
        s3 = 'WHERE id=%s' % self.dataCat_id
        try:
            cursor.execute(s1 + ' ' + s2 + ' ' + s3)
            connection.commit()
            connection.close()
            self.mainapp.cerrar_updateCat()
        except Exception as e:
            print('error')
            connection.close()

    def delete_data_Cat(self):
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        s = 'delete from CATEGORIAS where id=' + self.dataCat_id
        cursor.execute(s)
        connection.commit()
        connection.close()
        self.mainapp.cerrar_updateCat()

    def back_to_dbw_cat(self):
        self.mainapp.cerrar_updateCat()

######## aquitodobien
class DataWid_Pro(BoxLayout):
    def __init__(self, mainapp, **kwargs):
        super(DataWid_Pro,self).__init__()
        self.mainapp = mainapp

    def update_data_Pro(self, dataPro_id):
        print('actualizar producto')
        self.mainapp.goto_updatedataProd(dataPro_id)

class ProductosWid(BoxLayout):
     def __init__(self, mainapp, **kwargs):
         super(ProductosWid, self).__init__()
         self.mainapp = mainapp

         #print('aver que categoria es'+mainapp.dataCat_id)



     def cerrar_productoswid(self):
         self.mainapp.volveracatego_w()

     def check_memory_pro(self):

         #self.sele_idca = self.app.el_idca
         self.ids.container.clear_widgets()
         connection = sqlite3.connect(self.mainapp.DB_PATH)
         cursor = connection.cursor()
         #cursor.execute(''' SELECT PRODUCTOS.id, PRODUCTOS.nombre, PRODUCTOS.precio, PRODUCTOS.cantidad, PRODUCTOS.categoria_id FROM PRODUCTOS INNER JOIN CATEGORIAS WHERE PRODUCTOS.categoria_id =     ''')
         #cursor.execute("SELECT id, nombre, precio, cantidad FROM PRODUCTOS WHERE categoria_id = :categoria_id")
         cursor.execute ("SELECT id, nombre, precio, cantidad FROM PRODUCTOS WHERE categoria_id = :categoria_id", {"categoria_id" : self.mainapp.app.el_idca })
         for i in cursor:
             wid = DataWid_Pro(self.mainapp)
             r1 = 'ID Categoria:' + str(100000 + i[0])[1:9] + '\n'
             r2 = i[1] + '\n'
             r3 = 'Precio por unidad:' + '$' + str(i[2]) + '\n'
             r4 = 'Cantidad:' + str(i[3]) + '\n'
             wid.dataPro_id = str(i[0])
             wid.dataPro =  r2 + r3 + r4
             self.ids.container.add_widget(wid)
         wid = NuevoProButton(self.mainapp)
         self.ids.container.add_widget(wid)
         connection.close()

class NuevoProButton(MDRaisedButton):
    def __init__(self, mainapp, **kwargs):
        super(NuevoProButton, self).__init__()
        self.mainapp = mainapp

    def create_new_producto(self):
        # print('categoria es al intentar agregar producto'+ dataCat_id)
        self.mainapp.goto_insertPro()



class InsertProWid(BoxLayout):
    def __init__(self, mainapp,**kwargs):
        super(InsertProWid, self).__init__()
        self.mainapp =mainapp

        hoy = datetime.date.today()
        print(hoy)
        self.ids.insertarproducto_Fecha.text = str(hoy)

    def insertpro(self):
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        d1 = self.ids.insertarproducto_Nombre.text
        d2 = self.ids.insertarproducto_Precio.text
        d3 = self.ids.insertarproducto_Cantidad.text
        d4 = self.ids.category_elid.text
        d5 = self.ids.insertarproducto_Fecha.text

        a1 = (d1, d2, d3, d4, d5)
        s1 = 'INSERT INTO PRODUCTOS(nombre, precio, cantidad, categoria_id,  fechapro)'
        s2 = 'VALUES ("%s", %s, %s, "%s", "%s")' % a1

        # try:
        cursor.execute(s1 + '' +s2 )
        print('se ingreso el producto')
        connection.commit()
        connection.close()
        self.mainapp.cerrar_insertPro()
        # except Exception as e :
        #     print('error')
        #     connection.close()



    def back_to_dbw_pro(self):
        self.mainapp.cerrar_insertPro()

    def voz_botonP(self, texto):
        r = sr.Recognizer()
        print(texto)
        try:
            with sr.Microphone() as source:
                #r.adjust_for_ambient_noise(source)
                #print("Hable ahora...")
                audio = r.listen(source)
                entrada = r.recognize_google(audio, language='es-ES')
                if (texto=='NombreP'):
                    self.ids.insertarproducto_Nombre.text = entrada
                elif(texto=='PrecioP'):
                    self.ids.insertarproducto_Precio.text = entrada
                elif (texto == 'CantidadP'):
                    self.ids.insertarproducto_Cantidad.text = entrada


        except NotImplementedError:
            popup = ErrorPopup()
            popup.open()
        except :
            print("no entendi o tardo demasiado")

###prediccion

    def accion(self):
        print("esto va para la prediccion")
        APP_PATH = os.getcwd()
        DB_PATH = APP_PATH + '/database.db'
        con = sqlite3.connect(DB_PATH)  # CONEXION A LA BD
        cursor = con.cursor()  # CURSOR PARA EJECUTAR QUERYS
        producto = self.ids.insertarproducto_Nombre.text
        precio = self.ids.insertarproducto_Precio.text
        cantidad = self.ids.insertarproducto_Cantidad.text
        fecha = self.ids.insertarproducto_Fecha.text

        cursor.execute("""SELECT id FROM PRODUCTOS""")
        id_mayor = max(cursor)
        num_id = id_mayor[0]
        id_nuevo = num_id + 1
        print("El proximo id es: ", id_nuevo)
        datos = [id_nuevo, producto, precio, cantidad, fecha]
        try:
            cursor.execute("""INSERT INTO PRODUCTOS VALUES(?, ?, ?, ?, ?)""", datos)
            con.commit()
        except Exception as e:
            print(e)

        for i in datos:
            print(i)
        con.close()
        ####CREAR TXT FECHA
        self.creatxtFechas(producto, fecha, cantidad)
        ####CREAR TXT TABLA
        self.creatxtTabla(producto)
        ####CREAR TXT PREDICCION
        self.prediccion(producto, cantidad, fecha)

    def creatxtFechas(self, producto, fecha, cantidad):
        print("Crea el txt e inserta las fechas y cantidad de productos")
        archivo_fechas= open(producto+"_Fechas.txt", "a")
        archivo_fechas.write(cantidad+" "+fecha+"\n")
        archivo_fechas.close()
        archivo_tablas=open(producto+"_Tabla.txt", "a")
        #lin= archivo_tablas.read()
        archivo_tablas.close()
        return

    def creatxtTabla(self, producto):
        archivo = open(producto + "_Fechas.txt", "r")  # abrir el archivo-- el nombre no es estático

        lineas = archivo.readlines()  # se obtienen las lineas del archivo
        print(lineas)
        archivo.close()  # se cierra el archivo

        print(len(lineas))
        if (len(lineas) >= 2):  # se verifica que haya más de una linea de información
            ultima = lineas[len(lineas) - 1]
            print(len(ultima))
            penultima = lineas[len(lineas) - 2]
            print(len(penultima))

            if (len(ultima) == 14):  # se ontienen las fechas dependiendo del largo de las cadenas
                ultimaF = ultima[3:13]

            elif (len(ultima) == 13):
                ultimaF = ultima[2:12]

            if (len(penultima) == 14):
                penultimaF = penultima[3:13]
                cantidad = penultima[0:2]

            elif (len(penultima) == 13):
                penultimaF = penultima[2:12]
                cantidad = penultima[0]

            ultima_fecha = datetime.datetime.strptime(ultimaF, '%Y-%m-%d').date()  # se pasa la fecha a tipo date
            print(ultima_fecha)

            penultima_fecha = datetime.datetime.strptime(penultimaF, '%Y-%m-%d').date()  # se pasa la fecha a tipo date
            print(penultima_fecha)

            print("la cantidad de elementos es " + cantidad)

            dias = str((ultima_fecha - penultima_fecha).days)  # se obtiene el numero de días entre las fechas
            print(dias)

            datos = cantidad + " " + dias  # se crea la cadena que ingresa al nuevo txt
            print(datos)
            nuevo_archivo = open(producto + "_Tabla.txt", "a")
            nuevo_archivo.write(datos + "\n")
            nuevo_archivo.close()

        elif (len(lineas) == 1):
            print("datos insuficientes para generar regresión lineal")

        return

    def prediccion(self, producto, cantidad, fecha):
        print("seccion prediccion")
        fechaN = datetime.datetime.strptime(fecha, '%Y-%m-%d').date()
        archivo_datos = open(producto + "_Tabla.txt", "r")  # abrir el archivo
        renglones = archivo_datos.readlines()  # se obtienen los renglones del txt
        archivo_datos.close()

        print(renglones)
        x_numero_elementos = []
        y_dias = []

        for i in renglones:
            largo_cadena = len(i)
            if (largo_cadena == 4):
                numero = int(i[0])
                dias = int(i[2])
                x_numero_elementos.append(numero)
                y_dias.append(dias)

            elif (largo_cadena == 5):
                if (i[1] == " "):
                    numero = int(i[0])
                    dias = int(i[2:4])
                    x_numero_elementos.append(numero)
                    y_dias.append(dias)
                elif (i[2] == " "):
                    numero = int(i[0:2])
                    dias = int(i[3])
                    x_numero_elementos.append(numero)
                    y_dias.append(dias)
            elif (largo_cadena == 6):
                numero = int(i[0:2])
                dias = int(i[3:5])
                x_numero_elementos.append(numero)
                y_dias.append(dias)

        print(x_numero_elementos)
        print(y_dias)

        x = np.array(x_numero_elementos)
        print(x)
        y = np.array(y_dias)
        print(y)
        n = len(renglones)
        print(n)

        if (n == 0 or n == 1):
            print("No hay suficientes datos para generar la predicción")
            cadenaDialog = "No hay suficientes datos para generar la predicción"
        else:
            sumx = sum(x)
            print(sumx)
            sumy = sum(y)
            print(sumy)
            sumx2 = sum(x * x)
            print(sumx2)
            sumxy = sum(x * y)
            print(sumxy)
            promx = sumx / n
            print(promx)
            promy = sumy / n
            print(promy)

            m = ((n * sumxy) - (sumx * sumy)) / ((n * sumx2) - (sumx * sumx))
            b = promy - (m * promx)

            print(m, b)
            cant = int(cantidad)

            fx = int(m * cant + b)
            print("Tu producto pueden terminarse en ", fx, " dias")
            pred = fechaN + datetime.timedelta(days=fx)
            print("La fecha prevista para que se termine tu producto es: ", pred)
            fechaPred = str(pred)
            cadenaDialog = "La fecha prevista para que se termine tu producto es: " + fechaPred

            self.dialog = MDDialog(title="Prediccion de faltantes",
                                   # CUADROD DE DIALOGO PARA OBTENER EL PERIODO DEL REPORTE DE GASTOS
                                   text=cadenaDialog,
                                   size_hint=[.9, .9],
                                   auto_dismiss=True,
                                   buttons=[
                                       MDFlatButton(
                                           text="Cerrar",
                                           on_release=self.dialog_close)
                                   ]
                                   )
            self.dialog.open()
        return

    def dialog_close(self, *args):  # Cierra el dialog del boton ayuda
        # print("Cerrando Dialog")
        self.dialog.dismiss()


class UpdateProyeWid(BoxLayout):
    def __init__(self, mainapp, dataPro_id,**kwargs):
        super(UpdateProyeWid, self).__init__()
        self.mainapp = mainapp
        self.dataPro_id = dataPro_id
        self.check_memory_pro()

    def check_memory_pro(self):
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        s = 'SELECT nombre, precio, cantidad, fechapro FROM PRODUCTOS WHERE id='
        cursor.execute(s + self.dataPro_id)
        for i in cursor:
            # self.ids.in_idInv.text = str(i[0])
            self.ids.insertarproducto_Nombre.text = i[0]
            self.ids.insertarproducto_Precio.text = str(i[1])
            self.ids.insertarproducto_Cantidad.text = str(i[2])
            # self.ids.insertarproducto_Fecha.text = i[3]
        connection.close()

    def update_data_Pro(self):
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        d1 = self.ids.insertarproducto_Nombre.text
        d2 = self.ids.insertarproducto_Precio.text
        d3 = self.ids.insertarproducto_Cantidad.text

        a1 = (d1, d2, d3)
        s1 = 'UPDATE PRODUCTOS SET'
        s2 = 'nombre="%s", precio=%s, cantidad=%s  ' % a1
        s3 = 'WHERE id=%s' % self.dataPro_id
        try:
            cursor.execute(s1 + ' ' + s2 + ' ' + s3)
            connection.commit()
            connection.close()
            self.mainapp.cerrar_updatePro()
        except Exception as e:
            print('error')
            connection.close()

    def delete_data_Pro(self):
        connection = sqlite3.connect(self.mainapp.DB_PATH)
        cursor = connection.cursor()
        s = 'delete from PRODUCTOS where id=' + self.dataPro_id
        cursor.execute(s)
        connection.commit()
        connection.close()
        self.mainapp.cerrar_updatePro()

    def back_to_dbw_pro(self):
        self.mainapp.cerrar_updatePro()
