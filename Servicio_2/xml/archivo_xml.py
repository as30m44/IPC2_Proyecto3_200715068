import re
import xml.etree.ElementTree as ET
import os

from analizador.Palabra_listaes import Palabra_listaES
from analizador.Palabra import Palabra

class ArchivoXML():
  __listaArchivosXML = []
  __mensajes = Palabra_listaES()
  __diccionario = Palabra_listaES()
  __servicios = Palabra_listaES()
  __alias = Palabra_listaES()

  def __init__(self, nombreCarpeta):
    carpeta = nombreCarpeta + "/"
    listaArchivos = os.listdir(carpeta) # muestra la lista de todos los archivos XML en la carpeta
    # ______________________________________________________________________________________________
    # Agregar todos los archivos con extensión XML en un arreglo
    for archivoXML in listaArchivos:
      if (os.path.isfile(os.path.join(carpeta, archivoXML)) and archivoXML.endswith(".xml")):
        self.__listaArchivosXML.append(carpeta + archivoXML)
    # ______________________________________________________________________________________________
    self.__crearDiccionario()

  # ************************************************************************************************
  # creación del diccionario 
  def __crearDiccionario(self):
    terminos = {"es_fecha": 1, "es_hora": 2, "es_palabra":3 , "coma": 4, "punto": 5, "dos_puntos": 6, "lugar": 10, "y": 11, "fecha": 12, "usuario": 20 , "red": 30, "social": 31}
    for termino in terminos:
      palabra_i = Palabra()
      tipo = terminos[termino]
      palabra_i.set_termino(palabra_i)
      palabra_i.set_tipo(tipo)
      self.__diccionario.insertar(palabra_i)
  
  # ************************************************************************************************
  # agrega las palabras al diccionario 
  def actualizarDiccionario(self):
    # ______________________________________________________________________________________________
    # lee el contenido de cada archivo XML
    for archivoXML in self.__listaArchivosXML:
      arbol = ET.parse(archivoXML)
      # para etiqueta <diccionario> y <lista_mensajes>
      raiz = arbol.getroot()
      # ............................................................................................
      # en <diccionario> etiqueta: <sentimientos_positivos> <sentimientos_negativos> y <empresas_analizar>
      for nivel_2 in raiz[0]:
        contadorPalPos = 100
        contadorPalNeg = -100
        contadorEmpresa = 200
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        # para etiqueta <palabra> y <empresa>
        for nivel_3 in nivel_2:
          # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          if (nivel_2.tag == "sentimientos_positivos"):
            palabra_i = Palabra()
            palabra_i.set_termino = self.__normalizarPalabra(nivel_3.text)
            palabra_i.set_tipo = contadorPalPos
            self.__diccionario.insertar(palabra_i)
          elif (nivel_2.tag == "sentimientos_negativos"):
            palabra_i = Palabra()
            palabra_i.set_termino = self.__normalizarPalabra(nivel_3.text)
            palabra_i.set_tipo = contadorPalNeg
            self.__diccionario.insertar(palabra_i)
          elif (nivel_2.tag == "empresas_analizar"):
            # ......................................................................................
            # para etiqueta <nombre> y <servicio>
            for nivel_4 in nivel_3:
              if (nivel_4.tag == "nombre"):
                palabra_i = Palabra()
                palabra_i.set_termino = self.__normalizarPalabra(nivel_4.text)
                palabra_i.set_tipo = contadorEmpresa
                self.__diccionario.insertar(palabra_i)
                contadorEmpresa += 1
              elif (nivel_4.tag == "servicio"):
                palabra_i = Palabra()
                palabra_i.set_termino = nivel_4.attrib.get("nombre")
                palabra_i.set_tipo = contadorEmpresa - 1
                self.__servicios.insertar(palabra_i)
                # __________________________________________________________________________________
                # para etiqueta <alias>
                for nivel_5 in nivel_4:
                  palabra_i = Palabra()
                  palabra_i.set_termino = self.__normalizarPalabra(nivel_5.text)
                  palabra_i.set_tipo = contadorEmpresa - 1
                  self.__alias.insertar(palabra_i)
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
        mensaje = ""
        palabra_i = ""
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if (nivel_2.tag == "mensaje"):
          mensaje = nivel_2.text
          mensaje.lower()
          # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          # recorre letra por letra cada mensaje
          for indice in range(len(mensaje)):
            caracter = mensaje[indice]
            # ......................................................................................
            if (self.__esCaracterEspecial(caracter)):
              pass
            else:
              
            # ......................................................................................
          # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # ______________________________________________________________________________________________

  # ************************************************************************************************
  def __normalizarPalabra(self, palabra):
    palabra = str(palabra).lower()
    vocales = (
      ("á", "a"),
      ("é", "e"),
      ("í", "i"),
      ("ó", "o"),
      ("ú", "u"),
    )
    # ______________________________________________________________________________________________
    for a, b in vocales:
      palabra = palabra.replace(a, b)
    # ______________________________________________________________________________________________
    return palabra

  # ************************************************************************************************
  def __normarlizarCaracter(self, caracter):
    caracter = str(caracter).lower()
    # ______________________________________________________________________________________________
    if (caracter == "á"):
      caracter = "a"
    elif (caracter == "é"):
      caracter = "e"
    elif (caracter == "í"):
      caracter = "i"
    elif (caracter == "ó"):
      caracter = "o"
    elif (caracter == "ú"):
      caracter = "u"
    # ______________________________________________________________________________________________
    return caracter

  # ************************************************************************************************
  def __esCaracterEspecial(self, caracter):
    encontrado = False
    # ______________________________________________________________________________________________
    if (caracter == " "): # espacio
      encontrado = True
    elif (caracter == "\n"): # salto de línea
      encontrado = True
    elif (caracter == "\t"): # tabulador
      encontrado = True
    # ______________________________________________________________________________________________

  # ************************************************************************************************

    return encontrado
        # recorre el contenido dentro de las etiquetas <ciudad>
          # creación de objetos
          fila = Fila()
          unidadMilitar = UnidadMilitar()
          # ............................................................................................
          # caso 1: datos para el objeto Ciudad()
          if (nivel_3.tag == "nombre"):
            # busca si la ciudad está en la lista y devuelve su posición
            idCiudad = self.__listaCiudades.get_idCiudadxNombre(nivel_3.text) # 0: para nuevo o no existe ciudad
            # obtención de atributos de xml
            nombre = nivel_3.text
            noColumnas = int(nivel_3.attrib.get("columnas"))
            noFilas = int(nivel_3.attrib.get("filas"))
            # agregar atributos a objeto Ciudad()
            ciudad.set_nombre(nombre)
            ciudad.set_noColumnas(noColumnas)
            ciudad.set_noFilas(noFilas)
            ciudad_i += 1
          # ............................................................................................
          # caso 2: datos para el objeto Fila()|MAPA
          elif (nivel_3.tag == "fila"):
            # obtención de atributos de xml
            estado = ""
            estadoAux = nivel_3.text
            for i in range(0, len(estadoAux), 1):
              if (estadoAux[i] != "\""):
                estado += estadoAux[i]
            # agregar atributos a objeto Fila()
            fila.set_estado(estado)
            listaFilas.insertar(fila)
            filas_i += 1
          # ............................................................................................
          # caso 3: datos para el objeto UnidadMilitar()
          elif (nivel_3.tag == "unidadMilitar"):
            posicion_X = int(nivel_3.attrib.get("columna"))
            posicion_Y = int(nivel_3.attrib.get("fila"))
            capacidadCombate = int(nivel_3.text)
            # agregar atributos a objeto UnidadMilitar()
            unidadMilitar.set_posicion(posicion_X, posicion_Y)
            unidadMilitar.set_capacidadCombate(capacidadCombate)
            listaUnidadesMilitares.insertar(unidadMilitar)
            unidadesMilitares_i += 1
          # ............................................................................................
          # caso A: cuando ya es el último elemento del nivel_2
          totalNivel_2 = ciudad_i + filas_i + unidadesMilitares_i
          if (totalNivel_2 == len(nivel_2)):
            # __________________________________________________________________________________________
            # caso A.1: no hay datos de mapa y unidades militares
            if (filas_i == 0 and unidadesMilitares_i == 0):
              print("XML: no es posible almacenar datos, hace falta mapa")
            # __________________________________________________________________________________________
            # caso A.2: no hay datos de mapa
            elif (filas_i == 0 and unidadesMilitares_i != 0):
              print("XML: no es posible almacenar datos, hace falta mapa")
            # __________________________________________________________________________________________
            # caso A.3: hay únicamente datos de mapa
            elif (filas_i != 0 and unidadesMilitares_i == 0):
              ciudad.set_listaFilas(listaFilas)
              # caso A.3.1: cuando la ciudad no está en la lista o la lista esta vacía
              if (idCiudad == 0):
                self.__listaCiudades.insertar(ciudad)
              # caso A.3.2: cuando está la ciudad en la lista
              else:
                self.__listaCiudades.modificarCiudad(ciudad)
            # __________________________________________________________________________________________
            # caso A.4: hay datos de mapa y unidades militares
            else:
              ciudad.set_listaFilas(listaFilas)
              ciudad.set_listaUnidadesMilitares(listaUnidadesMilitares)
              # caso A.4.1: cuando la ciudad no está en la lista o la lista esta vacía
              if (idCiudad == 0):
                self.__listaCiudades.insertar(ciudad)
              # caso A.4.2: cuando está la ciudad en la lista
              else:
                self.__listaCiudades.modificarCiudad(ciudad)
    self.__crearListaRobot()
    return self.__listaCiudades  

  def get_listaRobotsRescate(self):
    return self.__listaRobotsRescate

  def get_listaRobotsExtraccion(self):
    return self.__listaRobotsExtraccion

  def get_matrizMapa(self, idCiudad):
    # ----------------------------------------------------------------------------------------------
    # creación del mapa
    self.__listaCiudades.ubicar(idCiudad)
    listaFilas = self.__listaCiudades.get_ciudad().get_listaFilas()
    # listaFilas.imprimir()
    ciudad = self.__listaCiudades.get_ciudad()
    noColumnas = ciudad.get_noColumnas()
    noFilas = ciudad.get_noFilas()
    self.__matrizMapa = Mapa_matriz(noColumnas, noFilas)
    # recorre cada fila de la "lista de filas"
    for idFila in range(1, noFilas + 1, 1):
      listaFilas.ubicar(idFila) # sitúo el apuntador en cada tupla
      fila = listaFilas.get_fila() # obtengo el objeto de la tupla seleccionada
      estado = fila.get_estado()
      # recorre la cadena de cada fila {****E****C****R****}
      for idColumna in range(0, len(estado), 1):
        mapa = Mapa()
        mapa.set_estado(estado[idColumna])
        mapa.set_posicion(idColumna + 1, idFila)
        self.__matrizMapa.insertar(mapa)
        # verificar la realización de misiones
        if (estado[idColumna] == "C" or estado[idColumna] == "c"): 
          self.__hayUnidadCivil = True
        elif (estado[idColumna] == "R" or estado[idColumna] == "r"):
          self.__hayRecursoMilitar = True
    # ----------------------------------------------------------------------------------------------
    # inserción de la unidades militares
    listaUnidadesMilitares = self.__listaCiudades.get_ciudad().get_listaUnidadesMilitares()
    if (listaUnidadesMilitares.estaVacio() == False):
      # listaUnidadesMilitares.imprimir()
      noFilas = listaUnidadesMilitares.get_noUnidadesMilitares()
      # recorre cada fila de las "unidades militares"
      for idFila in range(1, noFilas + 1, 1):
        # ubicar la unidad militar y obtener sus atributos
        listaUnidadesMilitares.ubicar(idFila)
        unidadMilitar = listaUnidadesMilitares.get_unidadMilitar()
        posicion_X = unidadMilitar.get_posicion_X()
        posicion_Y = unidadMilitar.get_posicion_Y()
        # reasignar atributos del mapa
        mapa = Mapa()
        mapa.set_estado("M")
        mapa.set_posicion(posicion_X, posicion_Y)
        self.__matrizMapa.ubicarNodoActual(posicion_X, posicion_Y)
        self.__matrizMapa.modificarMapa(mapa)
      # self.__matrizMapa.imprimir()
    return self.__matrizMapa

  def get_hayUnidadCivil(self):
    return self.__hayUnidadCivil

  def get_hayRecursoMilitar(self):
    return self.__hayRecursoMilitar
  # ---- crea los mensajes en una lista de palabras ----
  def get_mensajes(self):
    pass

  def __crearListaRobot(self):
    # **********************************************************************************************
    # Atributos del objeto Robot()
    idRobot = 0
    nombre = ""
    tipo = ""
    capacidad = 0
    # **********************************************************************************************
    # lee el contenido de cada archivo XML
    for archivoXML in self.__listaArchivosXML:
      arbol = ET.parse(archivoXML)
      raiz = arbol.getroot() # raiz[] es <robots>
      # recorre el contenido dentro de las etiquetas <robots>
      for nivel_2 in raiz[1]: # nivel_2 es <robot>
        robot = Robot()
        # ------------------------------------------------------------------------------------------
        # recorre el contenido dentro de las etiquetas <robot>
        for nivel_3 in nivel_2: # nivel_3 es <nombre>
          # ........................................................................................
          # caso 1: datos para el objeto Robot()
          if (nivel_3.tag == "nombre"):
            # obtención de atributos de xml
            nombre = nivel_3.text
            tipo = nivel_3.attrib.get("tipo")
            if (tipo == "ChapinFighter"):
              capacidad = int(nivel_3.attrib.get("capacidad"))
            else: 
              capacidad = 0
            # agregar atributos a objeto Ciudad()
            robot.set_nombre(nombre)
            robot.set_tipo(tipo)
            robot.set_capacidad(capacidad)
            # insertar el robot en la lista según su tipo
            # ......................................................................................
            # caso 1.1: robot tipo ChapinFighter
            if (tipo == "ChapinFighter"):
              # busca si el robot está en la lista y devuelve su posición
              idRobot = self.__listaRobotsExtraccion.get_idRobotxNombre(nivel_3.text) # 0: para nuevo o no existe ciudad
              # caso 1.1.1: cuando la ciudad no está en la lista o la lista esta vacía
              if (idRobot == 0):
                self.__listaRobotsExtraccion.insertar(robot)
              # caso 1.1.2: cuando está la ciudad en la lista
              else:
                self.__listaRobotsExtraccion.modificarRobot(robot)
            # ......................................................................................
            # caso 1.2: robot tipo ChapinRescue
            else:
              # busca si el robot está en la lista y devuelve su posición
              idRobot = self.__listaRobotsRescate.get_idRobotxNombre(nivel_3.text) # 0: para nuevo o no existe ciudad
              # caso 1.2.1: cuando la ciudad no está en la lista o la lista esta vacía
              if (idRobot == 0):
                self.__listaRobotsRescate.insertar(robot)
              # caso 1.2.2: cuando está la ciudad en la lista
              else:
                self.__listaRobotsRescate.modificarRobot(robot)
  # ************************************************************************************************
  # desglosar el mensaje en palabras

  def imprimirListaXML(self):
    contador = 1
    for archivo in self.__listaArchivosXML:
      print(str(contador) + "." + archivo)
      contador += 1
      
  # ************************************************************************************************
  # área de pruebas
  def main(self):
    
if '__name__' == '__main__':
  print("hola mundo")