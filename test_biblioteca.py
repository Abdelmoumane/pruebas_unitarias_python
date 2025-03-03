import pytest
from biblioteca import Libro, Biblioteca

# Pruebas para la clase Libro
def test_creacion_libro():
    libro = Libro("1984", "George Orwell", 1949)
    assert libro.titulo == "1984"
    assert libro.autor == "George Orwell"
    assert libro.anio == 1949
    assert not libro.prestado

def test_estado_libro():
    libro = Libro("1984", "George Orwell", 1949)
    assert "disponible" in str(libro)
    libro.prestado = True
    assert "prestado" in str(libro)

# Pruebas para la clase Biblioteca
@pytest.fixture
def biblioteca_vacia():
    return Biblioteca()

@pytest.fixture
def biblioteca_con_libros():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(Libro("1984", "George Orwell", 1949))
    biblioteca.agregar_libro(Libro("El principito", "Antoine de Saint-Exupéry", 1943))
    return biblioteca

def test_agregar_libro(biblioteca_vacia):
    libro = Libro("Nuevo Libro", "Autor X", 2020)
    biblioteca_vacia.agregar_libro(libro)
    assert len(biblioteca_vacia.libros) == 1
    assert biblioteca_vacia.libros[0].titulo == "Nuevo Libro"

def test_eliminar_libro(biblioteca_con_libros):
    biblioteca_con_libros.eliminar_libro("1984")
    assert biblioteca_con_libros.buscar_libro("1984") is None

def test_eliminar_libro_no_existente(biblioteca_con_libros):
    biblioteca_con_libros.eliminar_libro("Libro Fantasma")
    assert len(biblioteca_con_libros.libros) == 2  # No debe cambiar la cantidad

def test_buscar_libro_existente(biblioteca_con_libros):
    libro = biblioteca_con_libros.buscar_libro("1984")
    assert libro is not None
    assert libro.titulo == "1984"

def test_buscar_libro_no_existente(biblioteca_con_libros):
    assert biblioteca_con_libros.buscar_libro("Libro Fantasma") is None

def test_listar_libros(biblioteca_con_libros):
    lista = biblioteca_con_libros.listar_libros()
    assert len(lista) == 2
    assert "1984 de George Orwell (1949)" in lista[0]

def test_prestar_libro_disponible(biblioteca_con_libros):
    resultado = biblioteca_con_libros.prestar_libro("1984")
    assert resultado == "Has pedido prestado el libro '1984'."
    assert biblioteca_con_libros.buscar_libro("1984").prestado

def test_prestar_libro_prestado(biblioteca_con_libros):
    biblioteca_con_libros.prestar_libro("1984")  # Se presta una vez
    resultado = biblioteca_con_libros.prestar_libro("1984")  # Se intenta prestar de nuevo
    assert resultado == "El libro '1984' ya está prestado."

def test_prestar_libro_no_existente(biblioteca_con_libros):
    resultado = biblioteca_con_libros.prestar_libro("Libro Fantasma")
    assert resultado == "El libro 'Libro Fantasma' no se encuentra en la biblioteca."

def test_devolver_libro_prestado(biblioteca_con_libros):
    biblioteca_con_libros.prestar_libro("1984")
    resultado = biblioteca_con_libros.devolver_libro("1984")
    assert resultado == "Has devuelto el libro '1984'."
    assert not biblioteca_con_libros.buscar_libro("1984").prestado

def test_devolver_libro_no_prestado(biblioteca_con_libros):
    resultado = biblioteca_con_libros.devolver_libro("1984")
    assert resultado == "El libro '1984' no estaba prestado."

def test_devolver_libro_no_existente(biblioteca_con_libros):
    resultado = biblioteca_con_libros.devolver_libro("Libro Fantasma")
    assert resultado == "El libro 'Libro Fantasma' no se encuentra en la biblioteca."
