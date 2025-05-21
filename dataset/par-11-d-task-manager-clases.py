class Actividad:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.realizada = False

    def completar(self):
        self.realizada = True

    def detalles(self):
        return f"[{'✓' if self.realizada else '✗'}] {self.nombre} (Nivel {self.nivel})"

def ordenar_tareas(tareas):
    return sorted(tareas, key=lambda t: t.nivel)

def main():
    tareas = []

    while True:
        print("\n1. Nueva\n2. Ver\n3. Hecha\n4. Salida")
        opcion = input("> ")
        if opcion == "1":
            nombre = input("Descripción: ")
            nivel = int(input("Prioridad (1-3): "))
            tareas.append(Actividad(nombre, nivel))
        elif opcion == "2":
            for i, t in enumerate(ordenar_tareas(tareas), start=1):
                print(f"{i}. {t.detalles()}")
        elif opcion == "3":
            idx = int(input("Tarea #: ")) - 1
            if 0 <= idx < len(tareas):
                tareas[idx].completar()
        elif opcion == "4":
            break

if __name__ == "__main__":
    main()
