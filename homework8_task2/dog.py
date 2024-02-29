from canine import Canine

class Dog(Canine):  # Наслідування: class Dog -> Canine
    def __init__(self, name, breed, size, trained):
        super().__init__(name, breed, size)
        self.trained = trained

    def eat(self, food):  # Поліморфізм: перевизначення методу eat у підкласі
        return super().eat(food)

