import pytest
from motivharia.model.autor import Autor

@pytest.fixture
def autor():
    return Autor(1, "John Doe")

@pytest.mark.parametrize("nombre, expected_result", [
    ("John Doe", "1|John Doe"),
    ("Jane Smith", "1|Jane Smith"),
    ("Alice Johnson", "1|Alice Johnson")
])
def test_autor_read(autor, nombre, expected_result):
    autor.update(nombre)
    assert autor.read() == expected_result

def test_autor_delete(autor):
    autor.delete()
    assert autor.nombre is None