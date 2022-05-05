from logica.listas.nodoenlazadosimple import NodoEnlazadoSimple 
from logica.listas.mensaje import Mensaje

class Mensaje_nodoES(NodoEnlazadoSimple):
  __mensaje = None # Palabra()

  # ************************************************************************************************
  # métodos set
  def set_mensaje(self, mensaje):
    self.__mensaje = mensaje
  
  # ************************************************************************************************
  # métodos get
  def get_mensaje(self):
    return self.__mensaje

  # ************************************************************************************************
  # impresión de datos
  def imprimir(self, tipo):
    if (tipo == "titulo"):
      self.__mensaje.imprimirEncabezado()
    else:
      self.__mensaje.imprimirCelda()