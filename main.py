from enfermedad import Enfermedad
from comunidad import Comunidad

ebola = Enfermedad(infeccion_probable=0.3 , 
                    promedio_pasos=18)
curico = Comunidad(num_ciudadanos=2000,
                   promedio_conexion_fisica=8,
                   enfermedad=ebola,
                   num_infectados=10,
                   probabilidad_conexion_fisica=0.8)