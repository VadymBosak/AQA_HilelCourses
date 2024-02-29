from quadruped import Quadruped

class Canine(Quadruped):  # Наслідування: class Canine -> Quadruped
    def __init__(self, name, breed, size):
        super().__init__(name, breed)
        self.size = size

    def make_sound(self):  # Поліморфізм: різні класи можуть мати різні реалізації методу make_sound
        return "Woof!"

    def fetch(self, item):  # Інкапсуляція: метод, що викликається лише для класу Canine
        return f"{self.name} ({self.breed}) of size {self.size} is fetching {item}."

