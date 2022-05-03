from django.shortcuts import render, redirect
from django.template import loader
import requests
from django.http import HttpRequest, HttpResponse

from datetime import datetime
import os


class Persona():
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
    
def enviar_xml(request):
  p1 = Persona("Reina", "Solis")
  ahora = datetime.now()
  temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
  diccionario = {"nombre_persona":p1.nombre.upper, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"], "temasDelCurso":temasDelCurso}
  return render(request, 'enviar_xml.html', diccionario)

def cargar_xml(request):
  datosXml = loader.get_template("enviar_xml.html")
  mensaje = requests.post('http://localhost:5000/xml')
  contexto = mensaje.json()
  return HttpResponse(datosXml.render(contexto, request))

def enviar_datos(request):
  print(request.POST)
  
  return render(request, "formulario.html")
  