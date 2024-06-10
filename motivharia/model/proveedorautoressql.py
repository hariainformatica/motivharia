import sqlite3

from motivharia.model.proveedorautoresi import ProveedorAutoresI
from motivharia.model.listaautores import ListaAutores
from motivharia.model.autor import Autor

from motivharia.model.database import Database


class ProveedorAutoresSQL(ProveedorAutoresI):
    def __init__(self):
        self.db = Database()

    def getAutores(self):
        lista_autores = ListaAutores()
        cursor = self.db.getAll('autor')
        for row in cursor:
            autor = Autor(row[0], row[1])
            lista_autores.create(autor)

        self.db.close()
        return lista_autores
    
    def createAutor(self, autor):
        self.db.insert('autor', '(?, ?)', (int(autor.id), str(autor.nombre)))

        return autor
    
    def updateAutor(self, nombre, nuevo_nombre):
        self.db.update('autor', 'nombre=?', 'nombre=?', (nuevo_nombre, nombre))
        
        return Autor(-1, nuevo_nombre)
    
    def deleteAutor(self, nombre):
        self.db.delete('autor', 'nombre=?', (nombre,))
        
        return Autor(-1, nombre)

    def close(self, lista):
        pass