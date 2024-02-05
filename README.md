Proyecto Desarrollo Fase 1

Este proyecto implementa un sistema bancario que gestiona una cola de clientes con diferentes categorías de prioridad.
El código se organiza en clases y funciones para facilitar su mantenimiento y comprensión.


Clase Cliente

La clase Cliente representa a un cliente en el sistema bancario. Cada cliente tiene un nombre y una lista de categorías
que determinan su prioridad. La categoría puede ser "Platinum", "Embarazada" y/o "Discapacidad".


Clase ColaClientes

La clase ColaClientes implementa la cola de clientes. Los clientes se organizan en la cola según reglas de prioridad.
Los métodos principales incluyen la adición de clientes, eliminación de clientes al frente de la cola,
búsqueda de la posición de un cliente y la impresión de la lista de clientes.


Métodos en la Clase ColaClientes

agregar_cliente(nombre, categorias): Agrega un cliente a la cola según las reglas de prioridad.

eliminar_cliente(): Elimina el cliente al frente de la cola.

encontrar_posicion_cliente(nombre): Encuentra la posición de un cliente en la cola.

imprimir_lista_clientes(): Imprime la lista de clientes en la cola.

atender_cliente_platino(nombre): Añade un cliente Platinum a la cola.

atender_cliente_embarazada(nombre): Añade un cliente Embarazada a la cola.

atender_cliente_discapacidad(nombre): Añade un cliente con Discapacidad a la cola.


Clase PreguntaCategorias

La clase PreguntaCategorias facilita la interacción con el usuario para obtener las categorías del cliente. 
Incluye métodos para imprimir el menú y obtener las categorías seleccionadas por el usuario.


Función Principal: main()

La función principal main() ejecuta el bucle principal del sistema bancario.
Permite al usuario realizar diversas operaciones, como agregar clientes, eliminar clientes,
encontrar la posición de un cliente y imprimir la lista de clientes en orden de llegada y prioridad.


Ejecución del Programa

El programa se ejecuta llamando a main() cuando el código se ejecuta directamente. 
Al seleccionar la opción "5", el programa se cierra, proporcionando una salida ordenada.

