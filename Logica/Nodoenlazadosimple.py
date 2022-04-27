class NodoEnlazadoSimple():
  __siguiente = None # NodoEnlazadoSimple()
  
  def __init__(self):
    pass
  
  def get_siguiente(self):
    return self.__siguiente
  
  def set_siguiente(self, siguiente):
    self.__siguiente = siguiente