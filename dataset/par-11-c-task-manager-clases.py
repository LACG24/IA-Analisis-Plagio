class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.hecha = False

    def marcar_hecha(self):
        self.hecha = True

    def __str__(self):
        estado = "✓" if self.hecha else "✗"
        return f"[{estado}] {self.nombre} (Prioridad: {self.prioridad})"

class GestorTareas:
    def __init__(self):
        self.lista = []

    def agregar(self, nombre, prioridad):
        nueva = Tarea(nombre, prioridad)
        self.lista.append(nueva)

    def mostrar(self):
        print("\nLista de tareas:")
        for i, tarea in enumerate(sorted(self.lista, key=lambda t: t.prioridad)):
            print(f"{i + 1}. {tarea}")

    def completar(self, i):
        if 0 <= i < len(self.lista):
            self.lista[i].marcar_hecha()
        else:
            print("Índice inválido")

def iniciar():
    gestor = GestorTareas()
    while True:
        print("\n--- ADMINISTRADOR DE TAREAS ---")
        print("1. Añadir tarea")
        print("2. Mostrar tareas")
        print("3. Marcar como completada")
        print("4. Salir")
        accion = input("Elige: ")

        if accion == "1":
            titulo = input("Descripción: ")
            prio = int(input("Nivel de prioridad: "))
            gestor.agregar(titulo, prio)
        elif accion == "2":
            gestor.mostrar()
        elif accion == "3":
            num = int(input("Número de tarea: ")) - 1
            gestor.completar(num)
        elif accion == "4":
            break
        else:
            print("Comando inválido")

if __name__ == "__main__":
    iniciar()
