from Nodoenlazadosimple import Nodoenlazadosimple 
from Palabra import Palabra

class Palabra_nodoES(Nodoenlazadosimple):
  __palabra = None # Palabra()

  # ************************************************************************************************
  # métodos set
  def set_palabra(self, palabra):
    self.__palabra = palabra
  
  # ************************************************************************************************
  # métodos get
  def get_palabra(self):
    return self.__palabra

  # ************************************************************************************************
  # impresión de datos
  def imprimir(self, tipo):
    if (tipo == "titulo"):
      self.__palabra.imprimirEncabezado()
    else:
      self.__palabra.imprimirCelda()