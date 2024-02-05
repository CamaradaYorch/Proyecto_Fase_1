#Proyecto Desarrollo 1

#---------------------------------------------

# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre, categorias):
        """
        Inicializa un objeto Cliente con un nombre y categorías.
        :param nombre: 
        Nombre del cliente.
        :param categorias: 
        Lista de categorías del cliente (Platinum, Embarazada, Discapacidad).
        """
        self.nombre = nombre
        self.categorias = categorias
        self.siguiente = None

#---------------------------------------------

# Definición de la clase ColaClientes
class ColaClientes:
    def __init__(self):
        """
        Inicializa una cola de clientes vacía.
        """
        self.inicio = None
        self.fin = None

#---------------------------------------------

    def agregar_cliente(self, nombre, categorias):
        """
        Agrega un cliente a la cola según las reglas de prioridad.
        :param nombre: Nombre del cliente.
        :param categorias: Lista de categorías del cliente.
        """
        nuevo_cliente = Cliente(nombre, categorias)
        if not self.inicio:
            self.inicio = nuevo_cliente
            self.fin = nuevo_cliente
        else:
            # Verificar si el nuevo cliente tiene prioridad especial
            if "Platinum" in categorias:
                nuevo_cliente.siguiente = self.inicio
                self.inicio = nuevo_cliente
            elif "Embarazada" in categorias and "Discapacidad" in categorias:
                self.inicio.siguiente = nuevo_cliente
                self.inicio = nuevo_cliente
            else:
                actual = self.inicio
                while actual.siguiente and "Platinum" in actual.siguiente.categorias:
                    actual = actual.siguiente
                nuevo_cliente.siguiente = actual.siguiente
                actual.siguiente = nuevo_cliente
                if not nuevo_cliente.siguiente:
                    self.fin = nuevo_cliente

#---------------------------------------------

    def eliminar_cliente(self):
        """
        Elimina el cliente al frente de la cola.
        """
        if not self.inicio:
            print("La cola está vacía.")
        else:
            cliente_atendido = self.inicio
            self.inicio = self.inicio.siguiente
            if cliente_atendido:
                print(f"Cliente {cliente_atendido.nombre} atendido.")
            else:
                print("No hay clientes para atender.")

#---------------------------------------------

    def encontrar_posicion_cliente(self, nombre):
        """
        Encuentra la posición de un cliente en la cola.
        :param nombre: Nombre del cliente a buscar.
        """
        posicion = 1
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                print(f"El cliente {nombre} se encuentra en la posición {posicion}.")
                return
            actual = actual.siguiente
            posicion += 1
        print(f"El cliente {nombre} no se encuentra en la cola.")

#---------------------------------------------

    def imprimir_lista_clientes(self):
        """
        Imprime la lista de clientes en la cola.
        """
        actual = self.inicio
        if not actual:
            print("La cola está vacía.")
        else:
            print("\n--- Lista de Clientes ---")
            while actual:
                print(f"Nombre: {actual.nombre}, Categorías: {actual.categorias}")
                actual = actual.siguiente

#---------------------------------------------

    def atender_cliente_platino(self, nombre):
        """
        Añade un cliente Platinum a la cola.
        :param nombre: Nombre del cliente Platinum.
        """
        self.agregar_cliente(nombre, ["Platinum"])
        print(f"Cliente {nombre} atendido con prioridad Platinum.")

#---------------------------------------------

    def atender_cliente_embarazada(self, nombre):
        """
        Añade una cliente Embarazada a la cola.
        :param nombre: Nombre del cliente Embarazada.
        """
        self.agregar_cliente(nombre, ["Embarazada"])
        print(f"Cliente {nombre} atendido con prioridad Embarazada.")

#---------------------------------------------

    def atender_cliente_discapacidad(self, nombre):
        """
        Añade un cliente con Discapacidad a la cola.
        :param nombre: Nombre del cliente Discapacidad.
        """
        self.agregar_cliente(nombre, ["Discapacidad"])
        print(f"Cliente {nombre} atendido con prioridad Discapacidad.")

#---------------------------------------------

    def ordenar_cola_por_prioridad(self):
        """
        Método no necesario en este caso, ya que la cola 
        se ordena automáticamente al agregar clientes.
        """
        pass

#---------------------------------------------

# Clase para preguntar al usuario las categorías del cliente
class PreguntaCategorias:
    @staticmethod
    def imprimir_menu():
        """
        Imprime el menú de opciones del sistema bancario.
        """
        print("\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")
        print("---- Sistema Bancario ----")
        print("1. Agregar cliente a la fila")
        print("2. Eliminar cliente atendido")
        print("3. Encontrar posición de un cliente")
        print("4. Imprimir lista de clientes en orden de llegada y prioridad")
        print("5. Salir")
        print("\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")

    @staticmethod
    def obtener_categorias():
        """
        Pregunta al usuario las categorías del cliente.
        :return: Lista de categorías seleccionadas por el usuario.
        """
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

#---------------------------------------------

# Función principal
def main():
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
            if "Platinum" in categorias:
                cola.atender_cliente_platino(nombre_cliente)
            elif "Embarazada" in categorias:
                cola.atender_cliente_embarazada(nombre_cliente)
            elif "Discapacidad" in categorias:
                cola.atender_cliente_discapacidad(nombre_cliente)
            else:
                cola.agregar_cliente(nombre_cliente, categorias)

        elif opcion == "2":
            cola.eliminar_cliente()

        elif opcion == "3":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            cola.encontrar_posicion_cliente(nombre_cliente)

        elif opcion == "4":
            cola.imprimir_lista_clientes()

#---------------------------------------------

if __name__ == "__main__":
    main()