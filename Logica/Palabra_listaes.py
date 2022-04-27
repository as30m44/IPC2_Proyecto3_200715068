from Palabra_nodoes import Palabra_nodoES

class Palabra_listaES():
  __nodoInicio = None # Contenido_nodoES()
  __nodoFinal = None # Contenido_nodoES()
  __nodoActual = None # Contenido_nodoES()
  __noPalabras = 0
  # === set y get ===
  def __init__(self):
    pass

  def get_noPalabras(self):
    return self.__noPalabras

  def get_palabra(self):
    return self.__nodoActual.get_palabra()
  # === set y get ===

  # === modificar lista ===
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
  # === modificar lista ===