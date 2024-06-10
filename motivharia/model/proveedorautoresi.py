from motivharia.model.autor import Autor
from motivharia.model.listaautores import ListaAutores

class ProveedorAutoresI:
    def getAutores(self)->ListaAutores:
        pass

    def close(self):
        pass
