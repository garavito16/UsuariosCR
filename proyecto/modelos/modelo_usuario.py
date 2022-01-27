
from proyecto.config.mysqlconnection import connectToMySQL

class Usuario:

    def __init__(self,nombre,apellido,correo_electronico,created_at,id=0):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.created_at = created_at

    @classmethod
    def listarUsuarios(self):
        query = "SELECT * FROM usuarios;"
        lista = connectToMySQL("users_schema").query_db(query)
        listaUsuarios = []
        for user in lista:
            listaUsuarios.append(Usuario(user["nombre"],user["apellido"],user["correo_electronico"],user["created_at"],user["id"]))
        return listaUsuarios

    @classmethod
    def agregarUsuario(self,usuario):
        query = "INSERT INTO usuarios(nombre, apellido, correo_electronico, created_at) VALUES (%(nombre)s,%(apellido)s,%(correo_electronico)s,now());"
        id = connectToMySQL("users_schema").query_db(query,usuario)
        print(id)
        return id
