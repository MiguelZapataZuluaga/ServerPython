
import sys
import io
import subprocess
from flask import Flask,request, render_template,  make_response, render_template_string, send_from_directory

import serial
inde="""<html>
  <head>
    <title>SANOFI</title>
  </head>
  <body>
    <h1>Número recibido</h1>
    <p>El número recibido es: <span id="data"></span></p>

    <script>
      // Obtener el número desde el valor de la respuesta HTTP
      var data = '{{ response }}';

      // Asignar el número al contenido del elemento con el id 'data'
      document.getElementById('data').textContent = data;
    </script>
  </body>
</html>


"""

flag=1;



app = Flask(__name__)

#arduino_port = 'COM3'  # Reemplaza con el puerto correcto de tu Arduino
#baud_rate = 9600

#ser = serial.Serial(arduino_port, baud_rate)
global data
@app.route('/')

def index():


    numero1 = 25 # Número que deseas enviar
    numero2 = 60
     # Lee el contenido del archivo HTML
    with open('/home/miguelzapta/index.html', 'r') as file:
        html_content = file.read()

    # Reemplaza el marcador de posición con el número
    html_content = html_content.replace('{{ numero1 }}', str(numero1))
    html_content = html_content.replace('{{ numero2 }}', str(numero2))

    # Devuelve el contenido HTML como respuesta
    return html_content

def reload_server():
    subprocess.call(['touch', '/var/www/miguelzapta_pythonanywhere_com_wsgi.py'])







if flag==1:
    reload_server();




