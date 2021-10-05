import pickle
import sqlite3
import jsonpickle

from Dominio.Producto import Producto


class PersistenciaProducto:

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_mascota.sqlite")
        self.__crear_tabla()


    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PRODUCTO(id text primary key," \
                " nombre text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_producto(self,producto : Producto):
        cursor = self.con.cursor()
        query = "insert into GUITARRA(id , nombre ," \
                " precio,"\
                f" ?,?,?)"
        cursor.execute(query,(str(producto.id),producto.nombre,producto.precio))
        self.con.commit()

    @classmethod
    def save(cls, producto):
        binary_open = open("files/"+str(producto.id) + '.gui', mode='wb')
        pickle.dump(producto, binary_open)
        binary_open.close()

    @classmethod
    def load(cls, file_name):
        binary_open = open("files/"+file_name, mode='rb')
        producto = pickle.load(binary_open)
        binary_open.close()
        return producto

    @classmethod
    def save_json(cls, producto):
        text_open = open("files/"+str(producto.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(producto)
        text_open.write(json_gui)
        text_open.close()


    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_gui = text_open.readline()
        producto = jsonpickle.decode(json_gui)
        text_open.close()
        return producto