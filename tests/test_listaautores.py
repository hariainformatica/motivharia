import pytest

from motivharia.model.listaautores import ListaAutores
from motivharia.model.autor import Autor

def test_create():
    lista_autores = ListaAutores()
    lista_autores.create(Autor(lista_autores.getNewId(),"John Doe"))
    assert len(lista_autores.read()) == 1

def test_read():
    lista_autores = ListaAutores()
    lista_autores.create("John Doe")
    lista_autores.create("Jane Smith")
    assert len(lista_autores.read()) == 2

def test_update():
    lista_autores = ListaAutores()
    lista_autores.create(Autor(lista_autores.getNewId(),"John Doe"))
    lista_autores.update("John Doe", "John Smith")
    print(lista_autores.read())

def test_delete():
    lista_autores = ListaAutores()
    lista_autores.create(Autor(lista_autores.getNewId(),"John Doe"))
    lista_autores.delete("John Doe")
    assert len(lista_autores.read()) == 0

def test_delete_nonexistent_author():
    lista_autores = ListaAutores()
    lista_autores.create(Autor(lista_autores.getNewId(),"John Doe"))
    lista_autores.delete("Jane Smith")
    assert len(lista_autores.read()) == 1
