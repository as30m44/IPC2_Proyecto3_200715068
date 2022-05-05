from logica.listas.palabra_nodoes import Palabra_nodoES

class Palabra_listaES():
  __nodoInicio = None # Contenido_nodoES()
  __nodoFinal = None # Contenido_nodoES()
  __nodoActual = None # Contenido_nodoES()
  __noPalabras = 0
  
  def __init__(self):
    pass

  # ************************************************************************************************
  # métodos get
  def get_noPalabras(self):
    return self.__noPalabras

  def get_palabra(self):
    return self.__nodoActual.get_palabra()

  # buscar tipo de palabra
  def get_tipo(self, termino):
    # ______________________________________________________________________________________________
    if (self.estaVacio()):
      print("LISTA PALABRAS: la lista está vacía")
    # ______________________________________________________________________________________________
    else:
      self.__nodoActual = self.__nodoInicio
      encontrado = False
      # ............................................................................................
      while (encontrado == False and self.__nodoActual != None):
        termino_i = self.__nodoActual.get_palabra().get_termino()
        tipo_i = self.__nodoActual.get_palabra().get_tipo()
        if (termino == termino_i):
          encontrado = True
        else:
          self.__nodoActual = self.__nodoActual.get_siguiente()
      # ............................................................................................
      # caso 1: el id se encuentra dentro de la lista
      if (encontrado == False):
        print("LISTA PALABRAS: no se encuentra el término que ha ingresado")
        tipo_i = 3
      return tipo_i
    # ______________________________________________________________________________________________
    
  # ************************************************************************************************
  # modificación de listas
  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFinal == None

  def insertar(self, palabra):
    palabra.set_idPalabra(self.__noPalabras + 1)
    nodoNuevo = Palabra_nodoES()
    nodoNuevo.set_palabra(palabra)
    # 1: lista vacía
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
    # 2: la lista tiene 1 o mas elementos
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo 
    self.__noPalabras += 1

  # ************************************************************************************************
  # imprimir
  def imprimir(self):
    if (self.estaVacio()):
      print("LISTA PALABRAS: la lista esta vacía")
    else:
      nodo_m = self.__nodoInicio
      nodo_m.imprimir("titulo")
      while (nodo_m != None):
        nodo_m.imprimir("celda")
        nodo_m = nodo_m.get_siguiente()