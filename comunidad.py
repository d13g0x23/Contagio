import json
import random
from ciudadano import Ciudadano

with open('nombres&apellidos.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica):
        self.num_ciudadanos = num_ciudadanos
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.enfermedad = enfermedad
        self.num_infectados = num_infectados
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.ciudadanos = []
    
    def crear_ciudadanos_desde_json(self):
        nombres = datos['nombres']
        apellidos = datos['apellidos']

        for i in range(self.num_ciudadanos):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            id = i + 1
            ciudadano = Ciudadano(id, nombre, apellido, self, None)
            self.ciudadanos.append(ciudadano)
        