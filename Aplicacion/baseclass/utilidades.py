from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle

import kivy.utils

class Banner(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()

        with self.canvas.before:
            Color(rgb=(.9, .9, .9, 0.1)) #r g b transparencia
            self.rect = RoundedRectangle(radius=[(40.0,40.0),(40.0,40.0),(40.0,40.0),(40.0,40.0)])
        
        self.bind(pos = self.update_rect, size = self.update_rect)
        
        self.operation = kwargs["operation"]
        
        self.title = MDLabel(text = kwargs["title"],
                             pos_hint = {"center_x": .5, "top":.99},
                             size_hint = (.3,.2),
                             theme_text_color = "Primary", 
                             font_style= "Subtitle1",
                             halign = "center")
        
        self.text_field = MDTextFieldRect(pos_hint = {"center_x": .5, "top": .7},
                                          size_hint = (.4, .13),
                                          hint_text = "Ingresa el Valor",
                                          halign = "center")       
        
        self.button = MDRectangleFlatIconButton(on_release = self.ejecutar,                                        
                                               pos_hint = {"center_x":.5, "top": .5},
                                               size_hint = (.3,.1),
                                               icon = "math-compass",
                                               text = "Convertir")
        
        self.result = MDLabel(pos_hint = {"center_x": .5, "top": .3},
                              size_hint = (.5,.2),
                              halign = "center")
        
        self.add_widget(self.title)
        self.add_widget(self.text_field)
        self.add_widget(self.button)
        self.add_widget(self.result)
        
    def ejecutar(self, widget):
        if self.operation == "onza_gramo":
            self.onza_gramo(self.text_field.text)
            
        elif self.operation == "gramo_onza":
            self.gramo_onza(self.text_field.text)
            
        elif self.operation == "libra_gramo":
            self.libra_gramo(self.text_field.text)
            
        elif self.operation == "kilogramo_libra":
            self.kilogramo_libra(self.text_field.text)
        
        elif self.operation == "galon_litro":
            self.galon_litro(self.text_field.text)
            
        elif self.operation == "litro_galon":
            self.litro_galon(self.text_field.text)
            
        elif self.operation == "farenheit_celcius":
            self.farenheit_celcius(self.text_field.text)
            
        elif self.operation == "celcius_farenheit":
            self.celcius_farenheit(self.text_field.text)
            
           
    def onza_gramo(self, cantidad_onzas): #funcion que convierte onzas a gramos 
        try:
            gramos = float(cantidad_onzas) * 28.3495
            self.result.text = f'Resultado: {gramos:,.3f} gramos'
            self.result.theme_text_color = "Primary"

        except ValueError:
            self.result.text = "Carácteres no aceptados"
            self.result.theme_text_color = "Error"
            
    def gramo_onza(self, cantidad_gramos): #funcion que convierte gramos a onzas
         try:
            onzas = float(cantidad_gramos) / 28.3495
            self.result.text = f'Resultado: {onzas:,.3f} onzas'
            self.result.theme_text_color = "Primary"

         except ValueError:
                self.result.text = "Carácteres no aceptados"
                self.result.theme_text_color = "Error"
        
    def libra_gramo(self, cantidad_libras): #453.592
        try:
            gramos = float(cantidad_libras) * 453.592
            self.result.text = f'Resultado: {gramos:,.3f} gramos'
            self.result.theme_text_color = "Primary"

        except ValueError:
            self.result.text = "Carácteres no aceptados"
            self.result.theme_text_color = "Error"
        
    def kilogramo_libra(self, cantidad_kilogramos):
        try:
            kilogramos = (float(cantidad_kilogramos) * 1000 ) / 453.592
            self.result.text = f'Resultado: {kilogramos:,.3f} Libras'
            self.result.theme_text_color = "Primary"

        except ValueError:
            self.result.text = "Carácteres no aceptados"
            self.result.theme_text_color = "Error"
    
    def galon_litro(self, cantidad_galones):
        try:    
            litros = (float(cantidad_galones) * 3.78541)
            self.result.text = f'Resultado: {litros:,.3f} Litros'
            self.result.theme_text_color = "Primary"

        except ValueError:
            self.result.text = "Carácteres no aceptados"
            self.result.theme_text_color = "Error"
            
    def litro_galon(self, cantidad_litros):
        try:
            galones = (float(cantidad_litros) / 3.78541)
            self.result.text = f'Resultado: {galones:,.3f} Galones'
            self.result.theme_text_color = "Primary"

        except ValueError:
            self.result.text = "Carácteres no aceptados"
            self.result.theme_text_color = "Error"
    
    def farenheit_celcius(self, cantidad_farenheit):
        try:
            celcius = ((float(cantidad_farenheit) - 32) * (5/9))
            self.result.text = f'Resultado: {celcius:,.3f} °C'
            self.result.theme_text_color = "Primary"

        except ValueError:
            self.result.text = "Carácteres no aceptados"
            self.result.theme_text_color = "Error"
            
    def celcius_farenheit(self, cantidad_celcius):
        try:
            farenheit = ((float(cantidad_celcius) *(9/5)) + 32)
            self.result.text = f'Resultado: {farenheit:,.3f} °F'
            self.result.theme_text_color = "Primary"

        except ValueError:
            self.result.text = "Carácteres no aceptados"
            self.result.theme_text_color = "Error"
           
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
