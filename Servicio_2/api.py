from xml.etree.ElementTree import XMLParser
from datetime import datetime

from flask import Flask, Response, request
from flask import Flask, render_template
# import xmltodict
# from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import os
# from requests import request
# **************************************************************************************************
# Clase de ejemplo
class Persona():
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
# **************************************************************************************************

app = Flask(__name__)
# *************************************************************************
app.config['UPLOAD_FOLDER'] = 'D:/Documentos/Programacion/22S1IPC2/Proyecto_3/IPC2_Proyecto3_200715068/Servicio_2/xml/archivos'
# app.config['MAX_CONTENT_PATH']
# *************************************************************************

@app.route("/api/url", methods=['GET','POST'])  
def main():
    xml = '<?xml version="1.0" encoding="UTF-8"?><breakfast_menu><food><name>Belgian Waffles</name><calories>650</calories></food></breakfast_menu>'
    return Response(xml, mimetype='text/xml')
#linea eztra

@app.route("/api/xml", methods=['GET'])  
def xml():
    #xml = '<html><body><p>Hola</p></body></html>'
    return Response(request.data, mimetype='text/xml')

# *************************************************************************
# @app.route('/upload')
# def upload_file():
#    return render_template('formulario.html')
# **************************************************************************************************
# Recepción del mensaje
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
  # ________________________________________________________________________________________________
  # prueba para mostrar datos de una clase
  user = {'nickname': 'Miguel'} # fake user
  posts = [# fake array of posts
    {
      'author': { 'nickname': 'John' },
      'body': 'Beautiful day in Portland!'
    },
    {
      'author': { 'nickname': 'Susan' },
      'body': 'The Avengers movie was so cool!'
    }
  ]
  # ________________________________________________________________________________________________
  # if request.method == 'POST':
  # f.save(secure_filename(f.filename))
  # print(type(request.files['file']))
  # diccionario = XMLParser(resultado)
  # print(diccionario) #print(resultado[15])
  
  # f = request.files['file']
  # resultado = (f.stream.readlines())
  
  archivo = request.files['file']
  archivoNombre = secure_filename(archivo.filename)
  archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], archivoNombre))
  print(type(posts))
  resultado = archivo.stream.readlines()
  # return 'file uploaded successfully'
  if request.method == 'POST':
    print("petición POST") # el formulario lo define como post
  else:
    print("petición GET")
  # return Response(resultado, mimetype='text/xml')
  # ________________________________________________________________________________________________
  # respuesta de ejemplo
  return render_template("index.html", title = 'Home', user = user, posts = posts)

# **************************************************************************************************
# Ejecución de la api
if __name__ == "__main__": 
    app.run(debug=True)