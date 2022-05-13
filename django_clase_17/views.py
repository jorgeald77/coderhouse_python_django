from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context


def hello_world(request):
    return HttpResponse("Hola Coderhouse, from Django.")


def segunda_vista(request):
    return HttpResponse("Segnuda vista")


def vista_dia_hoy(request):
    hoy = datetime.now()
    return HttpResponse(f"La fecha es: {hoy}")


# Recibe parámetro por la URL, los tipos sólo son informativos
def mi_nombre_es(self, nombre: str, edad: int):
    return HttpResponse(f'Mi nombre es: {nombre} y tengo {edad} años.')


"""
Calcular año de nacimiento
    recibiendo la edad
"""


def anioNacimiento(self, edad: int):
    now = datetime.now()
    anio_nacimiento = now.year - edad
    return HttpResponse(f"Tu año de nacimiento es: {anio_nacimiento}")


def template(self):
    fileTemplate = open(
        '/Users/jorge/OneDrive/Coderhouse/Python/Django/django_clase_17/django_clase_17/templates/template.html')
    plantilla = Template(fileTemplate.read())
    fileTemplate.close()

    contexto = Context()
    html = plantilla.render(contexto)

    return HttpResponse(html)
