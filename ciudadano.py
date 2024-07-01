class Ciudadano:
    def __init__(self, id, nombre, apellido, comunidad, familia, estado=True):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.comunidad = comunidad
        self.familia = familia
        self.estado = estado
        self.susceptible = True
        self.infectado = False
        self.recuperado = False
        self.pasos_infectado = 0

    def infectar(self):
        if self.susceptible:
            self.susceptible = False
            self.infectado = True
            self.recuperado = False
            self.pasos_infectado = 0
    
    def recuperar(self):
        self.infectado = False
        self.recuperado = True