from colorama import init, Fore, Style # Esto es un detalle para añadir color mas tarde

init(autoreset=True)

class Tarea: # Creo una clase llamada tarea con 3 funciones 
    def __init__(self, descripcion):  # esta funcion crea una descripcion y marca la tarea como no completada
        self.descripcion = descripcion
        self.completada = False 

    def marcar_completada(self):   # esta funcion cambia la tarea a completada
        self.completada = True

    def __str__(self):  # esta funcion añade color y devuelve un str de la tarea y su estado
        estado = "completada" if self.completada else "pendiente"
        color = Fore.GREEN if self.completada else Fore.RED  # Verde para completada, rojo para pendiente
        return f"{color}{self.descripcion} - {estado}"

class ListaTareas:  # creo una nueva clase lista de tareas con las funciones que pide el enunciado
    def __init__(self): # creo una lista vacia
        self.tareas = []

    def agregar_tarea(self, descripcion):  # con esta funcion se crean nuevas tareas y la agrega a la lista vacia
        nueva_tarea = Tarea(descripcion)  
        self.tareas.append(nueva_tarea)
        print("Tarea agregada con éxito.") 

    def marcar_tarea_completada(self, posicion):  # con esta funcion marca las tareas completadas, como tiene que seleccionar una puede generar error asi que añado excepcion
        try:
            self.tareas[posicion].marcar_completada()
            print("Tarea marcada como completada.")
        except IndexError:
            print("Error: La posición indicada no existe")

    def mostrar_tareas(self): # con esta funcion muestra las tareas, estado y numero
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):  # esta funcion elimina tareas al indicar su posicion, de nuevo añado excepcion por si no se introduce una correcta
        try:
            self.tareas.pop(posicion)
            print("Tarea eliminada con éxito.")
        except IndexError:
            print("Error: La posición indicada no existe.")

def main():  # esta es la interfaz principal que vera el usuario
    lista_tareas = ListaTareas() # utiliza la clase lista tareas
    while True:
        print("\nGestor de Tareas Dani")  
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ") # segun la opcion que escoja el usuario llama a la funcion correspondiente de la clase
        if opcion == "1":            
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_tareas.agregar_tarea(descripcion)
        elif opcion == "2":     # las opciones en las que tiene que introducir una posicion añado excepciones.
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
            print("Saliendo del gestor de tareas Dani.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":  # para poder reutilizar el codigo cuando se utilice en otro script
    main()