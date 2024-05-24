from colorama import init, Fore, Style

init(autoreset=True)

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False 

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "completada" if self.completada else "pendiente"
        color = Fore.GREEN if self.completada else Fore.RED  # Verde para completada, rojo para pendiente
        return f"{color}{self.descripcion} - {estado}"

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print("Tarea agregada con éxito.")

    def marcar_tarea_completada(self, posicion):
        try:
            self.tareas[posicion].marcar_completada()
            print("Tarea marcada como completada.")
        except IndexError:
            print("Error: La posición indicada no existe")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        try:
            self.tareas.pop(posicion)
            print("Tarea eliminada con éxito.")
        except IndexError:
            print("Error: La posición indicada no existe.")

def main():
    lista_tareas = ListaTareas()
    while True:
        print("\nGestor de Tareas Dani")  
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: "))
                lista_tareas.marcar_tarea_completada(posicion)
            except ValueError:
                print("Error: Debe ingresar un número válido")
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
        elif opcion == "4":
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                lista_tareas.eliminar_tarea(posicion)
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        elif opcion == "5":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
