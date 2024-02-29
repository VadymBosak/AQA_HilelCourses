# file: feline.py

from quadruped import Quadruped

class Feline(Quadruped):  # Наслідування: class Feline -> Quadruped
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color

    def make_sound(self):  # Поліморфізм: різні класи можуть мати різні реалізації методу make_sound
        return "Meow!"

    def scratch(self):  # Інкапсуляція: метод, що викликається лише для класу Feline
        return f"{self.name} ({self.breed}) with {self.color} fur is scratching."


