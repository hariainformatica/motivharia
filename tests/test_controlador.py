import pytest

from motivharia.controlador import Controlador

@pytest.fixture
def controlador():
    return Controlador()

def test_obtenerMensajeSplash(controlador):
    assert controlador.obtenerMensajeSplash()['mensaje'] == "Motivharia"
    print(controlador.obtenerMensajeSplash())