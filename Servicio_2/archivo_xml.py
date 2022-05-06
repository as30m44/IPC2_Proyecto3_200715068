from logica.listas.mensaje_listaes import Mensaje_listaES
from logica.listas.palabra_listaes import Palabra_listaES
from logica.listas.palabra import Palabra
from logica.listas.mensaje import Mensaje
from validacion import Validacion

from pathlib import Path
import xml.etree.ElementTree as ET
import os

class Archivo_XML():
  __listaArchivosXML = []
  __mensajes = Mensaje_listaES()
  __diccionario = Palabra_listaES()
  __listaPalabras = Palabra_listaES()
  __validar = Validacion()

  def __init__(self, nombreCarpeta):
    carpeta = nombreCarpeta + "\\"
    listaArchivos = os.listdir(carpeta) # muestra la lista de todos los archivos XML en la carpeta
    # ______________________________________________________________________________________________
    # Agregar todos los archivos con extensión XML en un arreglo
    for archivoXML in listaArchivos:
      if (os.path.isfile(os.path.join(carpeta, archivoXML)) and archivoXML.endswith(".xml")):
        self.__listaArchivosXML.append(carpeta + archivoXML)
    # ______________________________________________________________________________________________
    self.__crearDiccionario()

  def imprimir(self):
    self.__diccionario.imprimir()
    print("\n")
    self.__desglosarMensajexPalabras()
    self.__listaPalabras.imprimir()
    print("\n")
    # self.__clasificarMensajes()
    # self.__mensajes.imprimir()
    print("\n")
  # ************************************************************************************************
  # creación del diccionario 
  def __crearDiccionario(self):
    terminos = {"lugar": 10, "y": 11, "fecha": 12, "usuario": 20 , "red": 30, "social": 31}
    for termino in terminos:
      palabra_i = Palabra()
      tipo = terminos[termino]
      palabra_i.set_termino(termino)
      palabra_i.set_tipo(tipo)
      self.__diccionario.insertar(palabra_i)
  
  # ************************************************************************************************
  # agrega las palabras al diccionario 
  def actualizarDiccionario(self):
    contadorPalPos = 100
    contadorPalNeg = -100
    contadorEmpresa = 0
    contadorServicio = 0
    contadorAlias = 0
    # ______________________________________________________________________________________________
    # lee el contenido de cada archivo XML
    for archivoXML in self.__listaArchivosXML:
      arbol = ET.parse(archivoXML)
      # para etiqueta <diccionario> y <lista_mensajes>
      raiz = arbol.getroot()
      # ............................................................................................
      # en <diccionario> etiqueta: <sentimientos_positivos> <sentimientos_negativos> y <empresas_analizar>
      for nivel_2 in raiz[0]:
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        # para etiqueta <palabra> y <empresa>
        for nivel_3 in nivel_2:
          # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          if (nivel_2.tag == "sentimientos_positivos"):
            palabra_i = Palabra()
            palabra_i.set_termino(self.__validar.normalizarPalabra(nivel_3.text))
            palabra_i.set_tipo(contadorPalPos)
            self.__diccionario.insertar(palabra_i)
          elif (nivel_2.tag == "sentimientos_negativos"):
            palabra_i = Palabra()
            palabra_i.set_termino(self.__validar.normalizarPalabra(nivel_3.text))
            palabra_i.set_tipo(contadorPalNeg)
            self.__diccionario.insertar(palabra_i)
          elif (nivel_2.tag == "empresas_analizar"):
            # ......................................................................................
            # para etiqueta <nombre> y <servicio>
            for nivel_4 in nivel_3:
              if (nivel_4.tag == "nombre"):
                contadorEmpresa += 1000
                contadorServicio = contadorEmpresa
                palabra_i = Palabra()
                palabra_i.set_termino(self.__validar.normalizarPalabra(nivel_4.text))
                palabra_i.set_tipo(contadorEmpresa)
                self.__diccionario.insertar(palabra_i)
              elif (nivel_4.tag == "servicio"):
                contadorServicio += 50
                palabra_i = Palabra()
                palabra_i.set_termino(nivel_4.attrib.get("nombre"))
                palabra_i.set_tipo(contadorServicio)
                self.__diccionario.insertar(palabra_i)
                # __________________________________________________________________________________
                # para etiqueta <alias>
                contadorAlias = contadorServicio
                for nivel_5 in nivel_4:
                  contadorAlias += 1
                  palabra_i = Palabra()
                  palabra_i.set_termino(self.__validar.normalizarPalabra(nivel_5.text))
                  palabra_i.set_tipo(contadorAlias)
                  self.__diccionario.insertar(palabra_i)
                # __________________________________________________________________________________
            # ......................................................................................
          # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          contadorPalPos += 1
          contadorPalNeg -= 1
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
      # ............................................................................................
    # ______________________________________________________________________________________________

  # ************************************************************************************************
  def __desglosarMensajexPalabras(self):
    # ______________________________________________________________________________________________
    # lee el contenido de cada archivo XML
    for archivoXML in self.__listaArchivosXML:
      arbol = ET.parse(archivoXML)
      # para etiqueta <diccionario> y <lista_mensajes>
      raiz = arbol.getroot()
      # ............................................................................................
      # en <lista_mensajes> etiqueta: <mensaje>
      for nivel_2 in raiz[1]:
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if (nivel_2.tag == "mensaje"):
          mensaje = nivel_2.text
          mensaje.lower()
          esFecha = False
          esHora = False
          esUsuario = False
          estado = 0
          lexema = ""
          # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # recorre letra por letra cada mensaje
          for indice in range(len(mensaje)):
            caracter = mensaje[indice]
            # ......................................................................................
            if (estado == 0): # inicio
              # ------------------------------------------------------------------------------------
              if (caracter.isalpha()): # LETRA
                caracter = self.__validar.normarlizarCaracter(caracter)
                lexema += caracter
                estado = 100
              elif (caracter.isdigit()): # DIGITO
                lexema += caracter
                estado = 200
              elif (self.__validar.esDelimitador(caracter)): # ESPACIO, TAB, ENTER
                estado = 0
                lexema = ""
              # ------------------------------------------------------------------------------------
            # ......................................................................................
            elif (estado == 100): # LETRA
              if (caracter.isalpha()): # LETRA
                caracter = self.__validar.normarlizarCaracter(caracter)
                lexema += caracter
                estado = 100
              elif (caracter == "_"): # GUION_BAJO
                lexema += caracter
                estado = 110
                esUsuario = True
              elif (caracter == "."): # PUNTO
                if (esUsuario):
                  lexema += caracter
                  estado = 110
                else:
                  palabra_i = Palabra()
                  palabra_i.set_tipo(self.__diccionario.get_tipoxTermino(lexema))
                  palabra_i.set_termino(lexema)
                  self.__listaPalabras.insertar(palabra_i)
                  estado = 0
                  lexema = ""
                  esUsuario = False
              elif (caracter == "@"): # ARROBA
                lexema += caracter
                estado = 120
                esUsuario = True
              elif (caracter.isdigit()): # DIGITO
                lexema += caracter
                estado = 130
                esUsuario = True
              else: # cualquier simbolo
                palabra_i = Palabra()
                if (esUsuario):
                  palabra_i.set_tipo(21)
                else:
                  palabra_i.set_tipo(self.__diccionario.get_tipoxTermino(lexema))
                palabra_i.set_termino(lexema)
                self.__listaPalabras.insertar(palabra_i)
                estado = 0
                lexema = ""
                esUsuario = False
            # ......................................................................................
            elif (estado == 110):
              if (caracter.isalpha()): # LETRA
                caracter = self.__validar.normarlizarCaracter(caracter)
                lexema += caracter
                estado = 100
              elif (caracter.isdigit() or self.__validar.esEmail(caracter)): # DIGITO
                lexema += caracter
                estado = 100
              else: # cualquier simbolo
                estado = 0
                lexema = ""
                esUsuario = False
            # ......................................................................................
            elif (estado == 120):
              if (caracter.isalpha()): # LETRA
                caracter = self.__validar.normarlizarCaracter(caracter)
                lexema += caracter
                estado = 110
              elif (caracter.isdigit() or self.__validar.esEmail(caracter)): # DIGITO
                lexema += caracter
                estado = 110
              else: # cualquier simbolo 
                estado = 0
                lexema = ""
                esUsuario = False
            # ......................................................................................
            elif (estado == 130):
              if (caracter.isalpha()): # LETRA
                caracter = self.__validar.normarlizarCaracter(caracter)
                lexema += caracter
                estado = 100
              elif (caracter.isdigit() or self.__validar.esEmail(caracter)): # DIGITO
                lexema += caracter
                estado = 100
              else: # cualquier simbolo
                palabra_i = Palabra()
                if (esUsuario):
                  palabra_i.set_tipo(21)
                else:
                  palabra_i.set_tipo(self.__diccionario.get_tipoxTermino(lexema))
                palabra_i.set_termino(lexema)
                self.__listaPalabras.insertar(palabra_i)
                estado = 0
                lexema = ""
                esUsuario = False
            # ......................................................................................
            elif (estado == 200): # DIGITO
              if (caracter.isdigit()):
                estado = 201
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 201): # DIAGONAL o DOS_PUNTOS
              if (caracter == "/"):
                estado = 210
                lexema += caracter
              elif (caracter == ":"):
                estado = 250
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 210): # DIGITO
              if (caracter.isdigit()):
                estado = 211
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 211): # DIGITO
              if (caracter.isdigit()):
                estado = 212
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 212): # DIAGONAL
              if (caracter == "/"):
                estado = 213
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 213): # DIGITO
              if (caracter.isdigit()):
                estado = 214
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 214): # DIGITO
              if (caracter.isdigit()):
                estado = 215
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 215): # DIGITO
              if (caracter.isdigit()):
                estado = 214
                lexema += caracter
              elif (self.__validar.esDelimitador(caracter) or (caracter.isalpha() or self.__validar.esSignoPuntuacion(caracter))):
                palabra_i = Palabra()
                palabra_i.set_termino(lexema)
                palabra_i.set_tipo(1)
                self.__listaPalabras.insertar(palabra_i)
                estado = 0
                lexema = ""
                indice -= 1
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 250): # DIGITO
              if (caracter.isdigit()):
                estado = 251
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 251): # DIGITO
              if (caracter.isdigit()):
                estado = 252
                lexema += caracter
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            elif (estado == 252): # DIGITO
              if (self.__validar.esDelimitador(caracter) or (caracter.isalpha() or self.__validar.esSignoPuntuacion(caracter))):
                palabra_i = Palabra()
                palabra_i.set_termino(lexema)
                palabra_i.set_tipo(2)
                self.__listaPalabras.insertar(palabra_i)
                estado = 0
                lexema = ""
                indice -= 1
              else:
                estado = 0
                lexema = ""
            # ......................................................................................
            else:
              print("descartar")
            # ......................................................................................
          palabra_j = Palabra()
          palabra_j.set_termino("--- MENSAJE ---")
          palabra_j.set_tipo(0)
          self.__listaPalabras.insertar(palabra_j)
          # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
      # ............................................................................................
    # ______________________________________________________________________________________________

  # ************************************************************************************************
  def __clasificarMensajes(self):
    noPalabras = self.__listaPalabras.get_noPalabras()
    estado = 0
    cadena = ""
    idPalabra = 1
    # Atributos
    lugar = ""
    fecha = ""
    hora = ""
    usuario = ""
    redSocial = ""
    # ______________________________________________________________________________________________
    while (idPalabra <= noPalabras):
      self.__listaPalabras.moverPuntero(idPalabra)
      tipo = self.__listaPalabras.get_palabra().get_tipo()
      termino = self.__listaPalabras.get_palabra().get_termino()
      # ............................................................................................
      if (tipo == 0):
        mensaje_i = Mensaje()
        palabrasPositivas = Palabra_listaES()
        palabrasNegativas = Palabra_listaES()
        mensaje_i.set_lugar(lugar)
        mensaje_i.set_fecha(fecha)
        mensaje_i.set_hora(hora)
        mensaje_i.set_usuario(usuario)
        mensaje_i.set_redSocial(redSocial)
        self.__mensajes.insertar(mensaje_i)
      # ............................................................................................
      else:
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if (estado == 0):
          if (tipo == 1): # FECHA
            fecha = termino
            estado = 0
          elif (tipo == 2): # HORA
            hora = termino
            estado = 0
          elif (tipo == 10): # LUGAR
            estado = 11
          elif (tipo == 20): # USUARIO
            estado = 21
          elif (tipo == 30): # RED
            estado = 31
          elif (100 <= tipo and tipo < 1000): # palabras_positivas y palabras_negativas
            estado = 100
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        elif (estado == 11): # Y
          if (tipo == 11):
            estado = 12
          else:
            estado = 0
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        elif (estado == 12): # FECHA
          if (tipo == 12):
            estado = 13
          else:
            estado = 0
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        elif (estado == 13): # Guatemala
          if (tipo == 3):
            estado = 13
            cadena += (termino + " ")
          else:
            lugar = cadena
            idPalabra -= 1
            estado == 0
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        elif (estado == 21): # as30m44
          if (tipo == 21):
            usuario = termino
            estado = 0
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        elif (estado == 31): # SOCIAL
          if (tipo == 31):
            estado = 32
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        elif (estado == 32): # FACEBOOK
          if (tipo == 3):
            redSocial = termino
            estado = 0
        # ............................................................................................
        elif (estado == 100):
          if (tipo > 0): # palabras_positivas
            pass
      # ............................................................................................
      idPalabra += 1
      print(idPalabra)
      print(termino)
      print(estado)
    # ______________________________________________________________________________________________

  # ************************************************************************************************
  # desglosar el mensaje en palabras

  def imprimirListaXML(self):
    contador = 1
    for archivo in self.__listaArchivosXML:
      print(str(contador) + "." + archivo)
      contador += 1
      
  # ************************************************************************************************
  # área de pruebas
  # def main(self):
    
if __name__ == '__main__':
  BASE_DIR = Path(__file__).resolve().parent.parent
  print(os.path.join(BASE_DIR, 'Servicio_2\\archivos'))
  archvoXML = Archivo_XML(os.path.join(BASE_DIR, 'Servicio_2\\archivos'))
  archvoXML.actualizarDiccionario()
  archvoXML.imprimir()

import re
cadena = "Vamos a aprender expresiones regulares en Python. Python es un leguaje de sintaxis sencilla."
textoBuscar = "aprender"
textoEncontrado = re.search(textoBuscar, cadena)
print(textoEncontrado.start()) #8
print(textoEncontrado.end()) #16
print(textoEncontrado.span()) #(8,16)

textoBuscar = "Python"
print(re.findall(textoBuscar, cadena)) #['Python', 'Python']

lista_nombres = [
  'Ana Gómez', 
  'María Martín',
  'Sandra López',
  'Santiago Martín',
  'Sandra Fernández'
  ]

for nombre in lista_nombres:
  if (re.findall('^Sandra', nombre)): #inicio con Sandra
    print(nombre)
  if (re.findall('Martín$', nombre)): #finalice con Martín
    print(nombre)

    'niñ[oa]'
    'niñ[^oa]' #neagcion
    '[0-3A-B]'
    '[0-3A-B]'
    
    'camión'
    'camion'
