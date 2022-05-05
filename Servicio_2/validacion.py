class Validacion():

  def __init__(self):
    pass

  # ************************************************************************************************
  def normalizarPalabra(self, palabra):
    palabra = str(palabra).lower()
    vocales = (
      ("á", "a"),
      ("é", "e"),
      ("í", "i"),
      ("ó", "o"),
      ("ú", "u"),
    )
    # ______________________________________________________________________________________________
    for a, b in vocales:
      palabra = palabra.replace(a, b)
    # ______________________________________________________________________________________________
    palabra = palabra.replace(" ", "")
    return palabra

  # ************************************************************************************************
  def normarlizarCaracter(self, caracter):
    caracter = str(caracter).lower()
    # ______________________________________________________________________________________________
    if (caracter == "á"):
      caracter = "a"
    elif (caracter == "é"):
      caracter = "e"
    elif (caracter == "í"):
      caracter = "i"
    elif (caracter == "ó"):
      caracter = "o"
    elif (caracter == "ú"):
      caracter = "u"
    # ______________________________________________________________________________________________
    return caracter

  # ************************************************************************************************
  def esDelimitador(self, caracter):
    encontrado = False
    # ______________________________________________________________________________________________
    if (caracter == " "): # espacio
      encontrado = True
    elif (caracter == "\n"): # salto de línea
      encontrado = True
    elif (caracter == "\t"): # tabulador
      encontrado = True
    # ______________________________________________________________________________________________
    return encontrado

    # ************************************************************************************************
  def esSignoPuntuacion(self, caracter):
    encontrado = False
    # ______________________________________________________________________________________________
    if (caracter == "."): 
      encontrado = True
    elif (caracter == ","):
      encontrado = True
    elif (caracter == ":"): 
      encontrado = True
    elif (caracter == ";"): 
      encontrado = True
    elif (caracter == "\""): 
      encontrado = True
    elif (caracter == "'"): 
      encontrado = True
    # ______________________________________________________________________________________________
    return encontrado
  
  # ************************************************************************************************
  def esEmail(self, caracter):
    encontrado = False
    # ______________________________________________________________________________________________
    if (caracter == "@"): # espacio
      encontrado = True
    elif (caracter == "."): # salto de línea
      encontrado = True
    # ______________________________________________________________________________________________
    return encontrado