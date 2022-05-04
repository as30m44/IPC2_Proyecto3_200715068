from Mensaje_nodoes import Mensaje_nodoES

class Palabra_listaES():
  __nodoInicio = None # Mensaje_nodoES()
  __nodoFinal = None # Mensaje_nodoES()
  __nodoActual = None # Mensaje_nodoES()
  __noMensajes = 0
  
  def __init__(self):
    pass

  # ************************************************************************************************
  # métodos get
  def get_noMensajes(self):
    return self.__noMensajes

  def get_mensaje(self):
    return self.__nodoActual.get_mensaje()

  # ************************************************************************************************
  # modificación lista
  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFinal == None

  def insertar(self, mensaje):
    mensaje.set_idMensaje(self.__noMensajes + 1)
    nodoNuevo = Mensaje_nodoES()
    nodoNuevo.set_mensaje(mensaje)
    # 1: lista vacía
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
    # 2: la lista tiene 1 o mas elementos
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo 
    self.__noMensajes += 1