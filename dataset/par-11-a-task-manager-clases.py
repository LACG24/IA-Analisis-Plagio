class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        estado = "✓" if self.completed else "✗"
        return f"[{estado}] {self.title} (Prioridad: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, priority):
        self.tasks.append(Task(title, priority))

    def list_tasks(self):
        print("\nTareas:")
        for idx, task in enumerate(sorted(self.tasks, key=lambda t: t.priority)):
            print(f"{idx + 1}. {task}")

    def complete_task(self, idx):
        if 0 <= idx < len(self.tasks):
            self.tasks[idx].complete()
        else:
            print("Índice fuera de rango")

def menu():
    tm = TaskManager()
    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Salir")
        op = input("Opción: ")

        if op == "1":
            t = input("Título: ")
            p = int(input("Prioridad (1=Alta, 3=Baja): "))
            tm.add(t, p)
        elif op == "2":
            tm.list_tasks()
        elif op == "3":
            idx = int(input("Índice de la tarea a completar: ")) - 1
            tm.complete_task(idx)
        elif op == "4":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()