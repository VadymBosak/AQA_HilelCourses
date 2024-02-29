from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def eat(self, food):  # Інкапсуляція: метод для здійснення дії їжі тварини, вбудований у базовий клас
        return f"{self.name} is eating {food}."




