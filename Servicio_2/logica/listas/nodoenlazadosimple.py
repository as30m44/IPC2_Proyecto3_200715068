class NodoEnlazadoSimple():
  __siguiente = None # NodoEnlazadoSimple()

  def __init__(self):
    pass

  # ************************************************************************************************
  # métodos set
  def set_siguiente(self, siguiente):
    self.__siguiente = siguiente
  
  # ************************************************************************************************
  # métodos get
  def get_siguiente(self):
    return self.__siguiente