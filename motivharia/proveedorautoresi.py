from motivharia.autor import Autor
from motivharia.listaautores import ListaAutores

class ProveedorAutoresI:
    def getAutores(self)->ListaAutores:
        pass

    def close(self):
        pass
