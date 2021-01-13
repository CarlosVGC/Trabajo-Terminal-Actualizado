from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton, MDIconButton
from kivy.uix.image import Image

class Sugerencias(FloatLayout): #Clase que crea las sugerencias del carrusel
    def __init__(self, **kwargs):
        super().__init__()
        self.pos_hint = {"x": .05, "y": .05}
        self.size_hint = .9, .9
        
        with self.canvas.before:
            Color(rgba=(0, .4, 0, 0.1))
            self.rect = RoundedRectangle(radius=[(20, 20)])
        self.bind(pos=self.update_rect, size=self.update_rect)


        self.titulo = MDLabel(text = kwargs["titulo"],
                              pos_hint={"center_x": .5, "top": .99},
                              size_hint=(.5, .1),
                              font_style = "H6",
                              halign = 'center'
                              )


        self.imagen = Image(pos_hint={"center_x": .5, "y": .0},
                            size_hint=(.9, .9),
                            source = kwargs["source"]
                            )
        
        self.botongustar = MDFillRoundFlatIconButton(pos_hint={"x": .05, "y": .05},
                                                text = "Útil",
                                                icon = "heart",
                                                #on_release = print("Hola")
                                                )
        
        self.botoncerrar = MDIconButton(pos_hint={"right": 1, "top": 1},
                                        icon = "close",
                                        on_release = kwargs["on_release"]
                                        )

        self.add_widget(self.titulo)
        self.add_widget(self.imagen)
        #self.add_widget(self.botongustar)
        #self.add_widget(self.botoncerrar)
        
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        
class SugerenciasScreen(Screen):
    carousel: object
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

        # Diccionario donde se guardan los titulos y las imagenes que se van a mostrar en la pantalla de sugerencias
        self.sugerencias = {"Plato del Buen Comer": "plato_buen_comer.jpg",
                            "Piramide Alimenticia": "piramide.jpeg",
                            "Beneficios de Tomar Agua": "tomar_agua.jpg",
                            "Como ser más ordenado": "orden.png"
                           # "": "",
                            }
    
    def on_kv_post(self, base_widget):
        self.carousel = self.ids["sugerencias_carousel"] #para poder trabajar desde python con el carousel
        # self.carousel.add_widget(Sugerencias(titulo ='Plato del buen comer', source = "imagenes/plato_buen_comer.jpg", on_release= self.my_callback))
        for titulo, ima in self.sugerencias.items():
            diapositiva = Sugerencias(titulo = titulo, source = f'imagenes/{ima}', on_release=self.my_callback)
            self.carousel.add_widget(diapositiva)
        
    def my_callback(self, widget):

        if self.carousel.current_slide is self.carousel.slides[-1]: #Si es la ultima diapositiva evita que se genere un error
            self.carousel.index -=1 #actualizando el indice del carrusel
            #print(self.carousel.index)
            self.carousel.remove_widget(self.carousel.current_slide) # Elimina la diapositiva
            self.carousel.load_previous()
            if not self.carousel.slides:
                self.carousel.add_widget(MDLabel(font_style="H2",
                                         halign = "center",
                                         text= "Actualmente no hay más sugerencias"
                                         ))
        else:
            self.carousel.remove_widget(self.carousel.current_slide)  # Elimina la diapositiva
            #self.carousel.load_previous()

    def on_pre_enter(self, *args):
        self.app.title = "Sugerencias"



