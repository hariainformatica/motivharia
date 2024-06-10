import csv

from motivharia.model.proveedorautoresi import ProveedorAutoresI
from motivharia.model.listaautores import ListaAutores
from motivharia.model.autor import Autor

class ProveedorAutoresCSV(ProveedorAutoresI):

    def getAutores(self) -> ListaAutores:
        lista_autores = ListaAutores()
        with open('data/autores.csv', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                autor = Autor(row[0], row[1])
                lista_autores.create(autor)
        return lista_autores

    def close(self, lista):
        with open('data/autores.csv', 'w') as file:
            writer = csv.writer(file, delimiter='|')
            for autor in lista.read():
                writer.writerow([autor.id, autor.nombre])
        file.close()
        
