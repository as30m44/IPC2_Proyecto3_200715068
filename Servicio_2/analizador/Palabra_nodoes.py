from Nodoenlazadosimple import Nodoenlazadosimple 
from Palabra import Palabra

class Palabra_nodoES(Nodoenlazadosimple):
  __palabra = None # Palabra()
  # === set y get ===
  def set_palabra(self, palabra):
    self.__palabra = palabra
  
  def get_palabra(self):
    return self.__palabra
  # === set y get ===

  # === imprimir en consola ===
  def imprimir(self, tipo):
    if (tipo == "titulo"):
      self.__palabra.imprimirEncabezado()
    else:
      self.__palabra.imprimirCelda()
  # === imprimir en consola ===