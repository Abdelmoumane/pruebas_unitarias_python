# biblioteca.py

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.prestado = False

    def __str__(self):
        estado = "prestado" if self.prestado else "disponible"
        return f"{self.titulo} de {self.autor} ({self.anio}) - {estado}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def listar_libros(self):
        return [str(libro) for libro in self.libros]

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro and not libro.prestado:
            libro.prestado = True
            return f"Has pedido prestado el libro '{libro.titulo}'."
        elif libro and libro.prestado:
            return f"El libro '{libro.titulo}' ya está prestado."
        else:
            return f"El libro '{titulo}' no se encuentra en la biblioteca."

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro and libro.prestado:
            libro.prestado = False
            return f"Has devuelto el libro '{libro.titulo}'."
        elif libro and not libro.prestado:
            return f"El libro '{libro.titulo}' no estaba prestado."
        else:
            return f"El libro '{titulo}' no se encuentra en la biblioteca."


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Menú de la Biblioteca ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Listar libros")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            anio = input("Año de publicación: ")
            libro = Libro(titulo, autor, anio)
            biblioteca.agregar_libro(libro)
            print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")
        elif opcion == "2":
            titulo = input("Título del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)
            print(f"El libro '{titulo}' ha sido eliminado de la biblioteca.")
        elif opcion == "3":
            print("Lista de libros en la biblioteca:")
            for libro in biblioteca.listar_libros():
                print(libro)
        elif opcion == "4":
            titulo = input("Título del libro a prestar: ")
            print(biblioteca.prestar_libro(titulo))
        elif opcion == "5":
            titulo = input("Título del libro a devolver: ")
            print(biblioteca.devolver_libro(titulo))
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")

if __name__ == "__main__":
    menu()
