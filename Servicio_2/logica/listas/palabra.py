class Palabra():
  __idPalabra = 0
  __termino = ""
  __tipo = 0
  def __init__(self):
    pass

  # ************************************************************************************************
  # métodos set
  def set_idPalabra(self, idPalabra):
    self.__idPalabra = idPalabra

  def set_termino(self, termino):
    self.__termino = termino

  def set_tipo(self, tipo):
    self.__tipo = tipo
    
  # ************************************************************************************************
  # métodos get
  def get_idPalabra(self):
    return self.__idPalabra

  def get_termino(self):
    return self.__termino

  def get_tipo(self):
    return self.__tipo

  # ************************************************************************************************
  # impresion de datos
  def imprimirEncabezado(self):
    idPalabra_ = "|" + "No".center(8, " ") + "|"
    tipo_ = "TIPO".center(8, " ") + "|"
    termino_ = "TERMINO".center(30, " ") + "|"
    print(idPalabra_, tipo_, termino_)

  def imprimirCelda(self):
    idPalabra_ = "|" + str(self.__idPalabra).center(8, " ") + "|"
    tipo_ = str(self.__tipo).center(8, " ") + "|"
    termino_ = str(self.__termino).center(30, " ") + "|"
    print(idPalabra_, tipo_, termino_)
