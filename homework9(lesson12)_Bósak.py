class Wagon:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if self.number != 1:
            if len(self.passengers) < 10:
                self.passengers.append(passenger)
            else:
                print("Вагон переповнений!")
        else:
            print("Локомотив не приймає пасажирів!")

    def __len__(self):
        return len(self.passengers)


class Train:
    def __init__(self):
        self.wagons = [Wagon(1)]  # Локомотив, який має номер 1

    def add_wagon(self):
        self.wagons.append(Wagon(len(self.wagons) + 1))

    def __len__(self):
        return len(self.wagons) - 1  # кіл-ть вагонів без локомотива

    def __str__(self):
        wagon_list = "-".join([f"[{wagon.number}]" for wagon in self.wagons[1:]])
        return f"<=[HEAD]-{wagon_list}"


train = Train()
train.add_wagon()
train.add_wagon()
train.wagons[1].add_passenger("Пасажир1")
train.wagons[1].add_passenger("Пасажир2")
train.wagons[2].add_passenger("Пасажир3")
print("Кількість вагонів без локомотива:", len(train))
print("Список вагонів без локомотива:", train)
for i, wagon in enumerate(train.wagons):
    print(f"Вагон {i + 1}: {wagon.passengers}")
train.wagons[0].add_passenger("Пасажир1")