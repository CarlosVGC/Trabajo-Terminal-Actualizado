import os   # Paquete para las funciones que requieren recursos del OS
import sqlite3 # biblioteca de la base de datos

from baseclass.inventario import *

APP_PATH = os.getcwd() # obtiene la dirección donde se úbican los archivos .py y .kv
DB_PATH = APP_PATH+'/database.db' # crea la base de datos

##******************** Base de datos - Creación ********************##
########### Conexión a la base de Datos ###########
def conexion_database(path):
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        crea_tabla_login(cursor)
        crea_tabla_categoria(cursor)
        crea_tabla_producto(cursor)
        crea_tabla_listadecompras(cursor)
        crea_tabla_productoporcomprar(cursor)

        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
#
############# Creamos las tablas en la base de datos #############
#
def crea_tabla_login(cursor):
    cursor.execute(login)
def crea_tabla_categoria(cursor):
    cursor.execute(comando1)
def crea_tabla_producto(cursor):
    cursor.execute(comando2)
def crea_tabla_listadecompras(cursor):
    cursor.execute(comando3)
def crea_tabla_productoporcomprar(cursor):
    cursor.execute(comando4)


        # Tabla login #
login = """ CREATE TABLE IF NOT EXISTS 
LOGIN(
    id          INTEGER     PRIMARY KEY,
    user_L    TEXT                    NOT NULL,
    email_L     TEXT                    NOT NULL,
    password    TEXT                    NOT NULL
)   """

        # Tabla categoria #
comando1 = """ CREATE TABLE IF NOT EXISTS
CATEGORIAS(
    id         INTEGER     PRIMARY KEY,
    nombre     TEXT,
    descripcion TEXT,
    usuario_id  INTEGER REFERENCES LOGIN(id),
    fechacat   DATE
    
)   """

        # Tabla productos #
comando2 = """ CREATE TABLE IF NOT EXISTS
PRODUCTOS(
    id          INTEGER     PRIMARY KEY,
    nombre    TEXT                NOT NULL,
    precio      FLOAT               NOT NULL,
    cantidad    INTEGER,
    
    categoria_id    INTEGER , 
    fechapro       DATE,
    FOREIGN KEY (categoria_id) REFERENCES  CATEGORIAS (id)     
)   """

# Tabla Lista de Compras #
comando3 = """ CREATE TABLE IF NOT EXISTS
LISTACOMPRAS(
    id          INTEGER     PRIMARY KEY,
    nombre    TEXT                NOT NULL,
    precio      FLOAT               NOT NULL,
    usuario_id    INTEGER REFERENCES LOGIN (id), 
    fechalis       DATE       
)   """

# Tabla productosporcomprar #

comando4 = """ CREATE TABLE IF NOT EXISTS
PRODUCTOSPORCOMPRAR(
    id          INTEGER     PRIMARY KEY,
    nombre    TEXT                NOT NULL,
    precio      FLOAT               NOT NULL,
    cantidad    INTEGER,
    
    categoria_id    INTEGER REFERENCES CATEGORIAS (id),
    lista_id        INTEGER REFERENCES LISTACOMPRAS (id) ,
    status      INTEGER, 
    fechaproco       DATE
     
)   """
##******************** Termina creación Base de datos ********************##

