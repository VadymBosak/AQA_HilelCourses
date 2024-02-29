from animal import Animal


class Quadruped(Animal):  # Наслідування: class Quadruped -> base class Animal
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def walk(self):  # Поліморфізм: різні класи можуть мати різні реалізації методу walk
        return f"{self.name} ({self.breed}) is walking on four legs."

    def eat(self, food):  # Інкапсуляція: метод для здійснення дії їжі тварини
        return super().eat(food)



