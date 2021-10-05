class Producto:

    def __init__(self, precio, nombre, id):
        self.precio=precio
        self.nombre=nombre
        self.id=id

    def __str__(self):
        return f"{self.precio} -- {self.nombre} -- {self.id}"

    def __repr__(self):
        return str(self.id)

    def cambiarPrecio(self, nuevo_precio):
        self.precio = nuevo_precio

    def cumple(self, especificacion):
        dict_producto = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_producto or dict_producto[k] != especificacion.get_value(k):
                return False
        return True