from logica.listas.nodoenlazadosimple import NodoEnlazadoSimple 
from logica.listas.palabra import Palabra

class Palabra_nodoES(NodoEnlazadoSimple):
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