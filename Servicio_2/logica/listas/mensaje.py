from logica.listas.palabra_listaes import Palabra_listaES

class Mensaje():
  __idMensaje = 0
  __tipo = ""
  __lugar = ""
  __fecha = ""
  __hora = ""
  __usuario = ""
  __redSocial = ""
  __noPalabrasPositivas = 0
  __noPalabrasNegativas = 0

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

  def set_noPalabrasPositivas(self, noPalabrasPositivas):
    self.__noPalabrasPositivas = noPalabrasPositivas

  def set_noPalabrasNegativas(self, noPalabrasNegativas):
    self.__noPalabrasNegativas = noPalabrasNegativas

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

  def get_noPalabrasPositivas(self):
    return self.__noPalabrasPositivas

  def get_noPalabrasNegativas(self):
    return self.__noPalabrasNegativas

  # ************************************************************************************************
  # impresión de datos
  def imprimirEncabezado(self):
    idMensaje_ = "|" + "No".center(8, " ") + "|"
    tipo_ = "TIPO".center(8, " ") + "|"
    lugar_ = "LUGAR".center(16, " ") + "|"
    fecha_ = "FECHA".center(16, " ") + "|"
    hora_ = "HORA".center(8, " ") + "|"
    usuario_ = "USUARIO".center(16, " ") + "|"
    redSocial_ = "RED SOCIAL".center(16, " ") + "|"
    positivo_ = "POSITIVO".center(8 , " ") + "|"
    negativo_ = "NEGATIVO".center(8 , " ") + "|"
    print(idMensaje_, tipo_, lugar_, fecha_, hora_, usuario_, redSocial_, positivo_, negativo_)

  def imprimirCelda(self):
    idMensaje_ = "|" + str(self.__idMensaje).center(8, " ") + "|"
    tipo_ = str(self.__tipo).center(8, " ") + "|"
    lugar_ = str(self.__lugar).center(16, " ") + "|"
    fecha_ = str(self.__fecha).center(16, " ") + "|"
    hora_ = str(self.__hora).center(8, " ") + "|"
    usuario_ = str(self.__usuario).center(16, " ") + "|"
    redSocial_ = str(self.__redSocial).center(16, " ") + "|"
    positivo_ = str(self.__noPalabrasPositivas).center(8, " ") + "|"
    negativo_ = str(self.__noPalabrasNegativas).center(8, " ") + "|"
    print(idMensaje_, tipo_, lugar_, fecha_, hora_, usuario_, redSocial_, positivo_, negativo_)
