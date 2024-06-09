from motivharia.autor import Autor

class ListaAutores:
    def __init__(self):
        self.autores = []

    def create(self, nombre):
        autor = Autor(nombre)
        self.autores.append(autor)

    def read(self):
        return self.autores

    def update(self, nombre, nuevo_nombre):
        for autor in self.autores:
            if autor.read() == nombre:
                autor.update(nuevo_nombre)

    def delete(self, nombre):
        for autor in self.autores:
            if autor.read() == nombre:
                autor.delete()
                self.autores.remove(autor)
                break