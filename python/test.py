class SimpleClass:
    def __new__(cls, parameters):
        instance = super(SimpleClass, cls).__new__(cls)
        print("Konstruktor: Tworzenie __new__ instancji klasy SimpleClass")
        return instance


    def __init__(self):
        print("Konstruktor: Tworzenie instancji klasy SimpleClass")

    def __del__(self):
        print("Destruktor: Usuwanie instancji klasy SimpleClass")

class ParameterizedClass:
    def __init__(self, value):
        self.value = value
        print(f"Konstruktor: Tworzenie instancji z wartością {self.value}")

    def __del__(self):
        print(f"Destruktor: Usuwanie instancji z wartością {self.value}")

class ResourceClass:
    def __init__(self):
        print("Konstruktor: Otwieranie zasobu (np. połączenie z bazą danych)")
        self.resource = "Zasób otwarty"

    def __del__(self):
        print("Destruktor: Zamykanie zasobu (np. połączenie z bazą danych)")

class InheritedClass(SimpleClass):
    def __init__(self):
        super().__init__()
        print("Konstruktor: Tworzenie instancji klasy InheritedClass")

    def __del__(self):
        print("Destruktor: Usuwanie instancji klasy InheritedClass")
        super().__del__()


simple = SimpleClass.__new__(simple,"hello")
param = ParameterizedClass(10)
resource = ResourceClass()
inherited = InheritedClass()

print("Hello")