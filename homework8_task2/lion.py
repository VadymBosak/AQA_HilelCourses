from feline import Feline

class Lion(Feline):  # Наслідування: class Lion -> Feline
    def __init__(self, name, breed, color, pride_name):
        super().__init__(name, breed, color)
        self.pride_name = pride_name

    def eat(self, food):  # Поліморфізм: перевизначення методу eat у підкласі
        return super().eat(food)
