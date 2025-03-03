# cine.py

class Pelicula:
    def __init__(self, nombre, asientos_disponibles, precio):
        self.nombre = nombre
        self.asientos_disponibles = asientos_disponibles
        self.precio = precio

    def vender_entradas(self, cantidad):
        if cantidad > self.asientos_disponibles:
            return f"No hay suficientes asientos disponibles. Solo quedan {self.asientos_disponibles} asientos."
        else:
            self.asientos_disponibles -= cantidad
            total = cantidad * self.precio
            return f"Has comprado {cantidad} entradas para {self.nombre}. Total: ${total}"

# Definir películas actuales
pelicula1 = Pelicula("Bridget Jones: Loca por él", 100, 8)
pelicula2 = Pelicula("Captain America: Brave New World", 50, 10)
pelicula3 = Pelicula("Paddington in Peru", 75, 9)

def main():
    print("Bienvenido al sistema de venta de entradas de cine")
    while True:
        print("\nPelículas disponibles:")
        print("1. Bridget Jones: Loca por él")
        print("2. Captain America: Brave New World")
        print("3. Paddington in Peru")
        print("4. Salir")

        opcion = input("Selecciona una película (1-4): ")

        if opcion == "1":
            pelicula_seleccionada = pelicula1
        elif opcion == "2":
            pelicula_seleccionada = pelicula2
        elif opcion == "3":
            pelicula_seleccionada = pelicula3
        elif opcion == "4":
            print("Gracias por usar el sistema de venta de entradas de cine. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        cantidad = int(input(f"¿Cuántas entradas deseas comprar para {pelicula_seleccionada.nombre}? "))

        print(pelicula_seleccionada.vender_entradas(cantidad))

if __name__ == "__main__":
    main()
