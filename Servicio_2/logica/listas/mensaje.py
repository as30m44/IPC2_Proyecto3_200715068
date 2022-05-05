from logica.listas.palabra_listaes import Palabra_listaES

class Mensaje():
  __idMensaje = 0
  __tipo = ""
  __lugar = ""
  __fecha = ""
  __hora = ""
  __usuario = ""
  __redSocial = ""
  __palabrasPositivas = Palabra_listaES()
  __palabrasNegativas = Palabra_listaES()

  def __init__(self):
    pass

  # ************************************************************************************************
  # métodos set
  def set_idMensaje(self, idMensaje):
    self.__idMensaje = idMensaje
    
  def set_tipo(self, tipo):
    self.__tipo = tipo

  def set_lugar(self, lugar):
    self.__lugar = lugar

  def set_fecha(self, fecha):
    self.__fecha = fecha

  def set_hora(self, hora):
    self.__hora = hora

  def set_usuario(self, usuario):
    self.__usuario = usuario

  def set_redSocial(self, redSocial):
    self.__redSocial = redSocial

  def set_palabrasPositivas(self, palabrasPositivas):
    self.__palabrasPositivas = palabrasPositivas

  def set_palabrasNegativas(self, palabrasNegativas):
    self.__palabrasNegativas = palabrasNegativas

  # ************************************************************************************************
  # métodos set
  def get_idMensaje(self):
    return self.__idMensaje

  def get_tipo(self):
    return self.__tipo

  def get_lugar(self):
    return self.__lugar

  def get_fecha(self):
    return self.__fecha

  def get_hora(self):
    return self.__hora

  def get_usuario(self):
    return self.__usuario

  def get_redSocial(self):
    return self.__redSocial

  def get_palabrasPositivas(self):
    return self.__palabrasPositivas

  def get_palabrasNegativas(self):
    return self.__palabrasNegativas

  # ************************************************************************************************
  # impresión de datos
  def imprimirEncabezado(self):
    idMensaje_ = "|" + "No".center(8, " ") + "|"
    tipo_ = "TIPO".center(30, " ") + "|"
    lugar_ = "LUGAR".center(8, " ") + "|"
    fecha_ = "FECHA".center(8, " ") + "|"
    hora_ = "HORA".center(8, " ") + "|"
    usuario_ = "USUARIO".center(8, " ") + "|"
    redSocial_ = "RED SOCIAL".center(8, " ") + "|"
    print(idMensaje_, tipo_, lugar_, fecha_, hora_, usuario_, redSocial_)

  def imprimirCelda(self):
    idMensaje_ = "|" + str(self.__idPalabra).center(8, " ") + "|"
    termino_ = str(self.__termino).center(30, " ") + "|"
    tipo_ = str(self.__tipo).center(8, " ") + "|"
    lugar_ = str(self.__lugar).center(8, " ") + "|"
    fecha_ = str(self.__fecha).center(8, " ") + "|"
    hora_ = str(self.__hora).center(8, " ") + "|"
    usuario_ = str(self.__usuario).center(8, " ") + "|"
    redSocial_ = str(self.__redSocial).center(8, " ") + "|"
    print(idMensaje_, tipo_, lugar_, fecha_, hora_, usuario_, redSocial_)
