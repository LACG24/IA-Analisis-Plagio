# Dynamic method creation and assignment
class Calculator:
    
    
# Adding dynamic methods
calc = Calculator()
calc.add_operation("add", lambda x, y: x + y)
calc.add_operation("subtract", lambda x, y: x - y)

def add_operation(self, name, func):
        self.operations[name] = func
        setattr(self, name, func)


def __init__(self):
        self.operations = {}
