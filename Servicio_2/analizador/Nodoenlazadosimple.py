class NodoEnlazadoSimple():
  __siguiente = None # NodoEnlazadoSimple()
  # === set y get ===
  def __init__(self):
    pass
  
  def set_siguiente(self, siguiente):
    self.__siguiente = siguiente
  
  def get_siguiente(self):
    return self.__siguiente
  # === set y get ===