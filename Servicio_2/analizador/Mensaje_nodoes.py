from Nodoenlazadosimple import Nodoenlazadosimple 
from Mensaje import Mensaje

class Mensaje_nodoES(Nodoenlazadosimple):
  __mensaje = None # Palabra()
  # === set y get ===
  def set_mensaje(self, mensaje):
    self.__mensaje = mensaje
  
  def get_mensaje(self):
    return self.__mensaje
  # === set y get ===

  # === imprimir en consola ===
  def imprimir(self, tipo):
    if (tipo == "titulo"):
      self.__mensaje.imprimirEncabezado()
    else:
      self.__mensaje.imprimirCelda()
  # === imprimir en consola ===