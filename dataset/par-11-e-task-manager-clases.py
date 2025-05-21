def crear_tarea(nombre, prioridad):
    return {"nombre": nombre, "prioridad": prioridad, "completada": False}

def mostrar_tareas(tareas):
    for i, tarea in enumerate(sorted(tareas, key=lambda x: x["prioridad"])):
        status = "✓" if tarea["completada"] else "✗"
        print(f"{i + 1}. [{status}] {tarea['nombre']} (P: {tarea['prioridad']})")

def gestor():
    tareas = []
    while True:
        print("\n1. Añadir")
        print("2. Listar")
        print("3. Completar")
        print("4. Salir")
        op = input("> ")

        if op == "1":
            n = input("Nombre de tarea: ")
            p = int(input("Prioridad (1-3): "))
            tareas.append(crear_tarea(n, p))
        elif op == "2":
            mostrar_tareas(tareas)
        elif op == "3":
            i = int(input("Índice a completar: ")) - 1
            if 0 <= i < len(tareas):
                tareas[i]["completada"] = True
        elif op == "4":
            break

if __name__ == "__main__":
    gestor()