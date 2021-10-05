from Dominio.Usuario import Usuario

class Admin(Usuario):

    def __init__(self, pin):
        self.pin=pin
