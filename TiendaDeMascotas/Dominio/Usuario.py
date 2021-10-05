class Usuario:

    def __init__(self, nombre, id):
        self.nombre=nombre
        self.id=id

    def __str__(self):
        return f"{self.nombre} -- {self.id} "

    def __repr__(self):
        return str(self.id)