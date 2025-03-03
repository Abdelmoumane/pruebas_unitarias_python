import pytest
from cine import Pelicula

def test_compra_exitosa():
    pelicula = Pelicula("Test Movie", 50, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Test Movie. Total: $50"
    assert pelicula.asientos_disponibles == 45
    

def test_compra_insuficientes_asientos():
    pelicula = Pelicula("Test Movie", 3, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."
    assert pelicula.asientos_disponibles == 3

def test_compra_cero_entradas():
    pelicula = Pelicula("Test Movie", 20, 10)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Test Movie. Total: $0"
    assert pelicula.asientos_disponibles == 20

def test_compra_todos_los_asientos():
    pelicula = Pelicula("Test Movie", 10, 10)
    resultado = pelicula.vender_entradas(10)
    assert resultado == "Has comprado 10 entradas para Test Movie. Total: $100"
    assert pelicula.asientos_disponibles == 0
