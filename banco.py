# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre, categorias):
        self.nombre = nombre
        self.categorias = categorias
        self.siguiente = None

# Definición de la clase NodoArbol
class NodoArbol:
    def __init__(self, cliente):
        self.cliente = cliente
        self.hijos = []

# Definición de la clase ArbolColaPrioridades
class ArbolColaPrioridades:
    def __init__(self):
        self.raiz = None

    def agregar_cliente(self, cliente):
        nuevo_nodo = NodoArbol(cliente)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._agregar_cliente(self.raiz, nuevo_nodo)

    def _agregar_cliente(self, nodo_actual, nuevo_nodo):
        if len(nodo_actual.hijos) == 0:
            nodo_actual.hijos.append(nuevo_nodo)
        else:
            for hijo in nodo_actual.hijos:
                # Ajusta las reglas de prioridad según tus necesidades
                if nuevo_nodo.cliente.categorias > hijo.cliente.categorias:
                    nodo_actual.hijos.insert(nodo_actual.hijos.index(hijo), nuevo_nodo)
                    return
            nodo_actual.hijos.append(nuevo_nodo)

    def imprimir_arbol(self):
        self._imprimir_arbol(self.raiz)

    def _imprimir_arbol(self, nodo_actual):
        if nodo_actual:
            print(f"Cliente: {nodo_actual.cliente.nombre}, Categorías: {nodo_actual.cliente.categorias}")
            for hijo in nodo_actual.hijos:
                self._imprimir_arbol(hijo)

# Definición de la clase ColaClientes
class ColaClientes:
    def __init__(self):
        self.arbol_prioridades = ArbolColaPrioridades()

    def agregar_cliente(self, nombre, categorias):
        nuevo_cliente = Cliente(nombre, categorias)
        self.arbol_prioridades.agregar_cliente(nuevo_cliente)

    def imprimir_lista_clientes(self):
        print("\n--- Lista de Clientes en Cola de Prioridades ---")
        self.arbol_prioridades.imprimir_arbol()

    # Resto de los métodos de la clase ColaClientes permanecen sin cambios

# Clase para preguntar al usuario las categorías del cliente
class PreguntaCategorias:
    @staticmethod
    def imprimir_menu():
        print("\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")
        print("---- Sistema Bancario ----")
        print("1. Agregar cliente a la fila")
        print("2. Eliminar cliente atendido")
        print("3. Encontrar posición de un cliente")
        print("4. Imprimir lista de clientes en orden de llegada y prioridad")
        print("5. Salir")
        print("\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")

    @staticmethod
    def obtener_categorias():
        platino = input("¿Es cliente Platinum? (1: Sí / 2: No): ") == "1"
        embarazada = input("¿Es mujer embarazada? (1: Sí / 2: No): ") == "1"
        discapacidad = input("¿Tiene discapacidad? (1: Sí / 2: No): ") == "1"

        categorias = []
        if platino:
            categorias.append("Platinum")
        if embarazada:
            categorias.append("Embarazada")
        if discapacidad:
            categorias.append("Discapacidad")

        return categorias

# Función principal
def banco():
    cola = ColaClientes()
    while True:
        print(" = " * 35)
        PreguntaCategorias.imprimir_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            print(" ▀" * 35)
            print("\n░░░░░   Haz Salido del programa   ░░░░░\n")
            print(" ▀" * 35)
            break

        if opcion == "1":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            categorias = PreguntaCategorias.obtener_categorias()
            cola.agregar_cliente(nombre_cliente, categorias)

        elif opcion == "2":
            cola.eliminar_cliente()

        elif opcion == "3":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            cola.encontrar_posicion_cliente(nombre_cliente)

        elif opcion == "4":
            cola.imprimir_lista_clientes()

if __name__ == "__main__":
    banco()
