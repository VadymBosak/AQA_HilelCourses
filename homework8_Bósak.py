# 1) Класс вашого рахунку банківського рахунку.
# Обов'язкові методи: покласти на рахунок, зняти з рахунку, подивитись баланс.
# Баланс напряму міняти не можна(підказка: тут краще за все робити через атрибут __balance ),
# використовуйте методи  ядл поповнення та зняття коштів з рахунку
#
# Зняти гроші можна при умові що їх достатньо на рахунку
#
# Використати як мінімум по 1 разу елементи: public, protected, privat атрибути, гетери, сетери, staticmethod та classmethod
#
# Приклад ініціації класу. не обов'язково саме такий, це концепт
#
# my_user_account = UserAccount(name, card_number, cvv, date, balance)

class UserAccount:
    def __init__(self, name, card_number, cvv, date, balance):
        self.name = name #public
        self._card_number = card_number #private
        self.__cvv = cvv #protected
        self.__date = date #protected
        self.__balance = balance #protected

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print('Withdrawal successful')
        else:
            print('Insufficient funds')

    def check_balance(self):
        return self.__balance

    #getter
    def get_card_number(self):
        return(self._card_number)

    #setter
    def set_card_number(self, card_number):
        self._card_number = card_number

    #getter
    def set_cvv(self, cvv):
        return self.__cvv

    def set_cvv(self, cvv):
        self.__cvv = cvv

    @staticmethod
    def validate_card_number(card_number):
        return len(card_number) == 16

    @classmethod
    def from_string(cls, user_data):
        name, card_number, cvv, date, balance = user_data.split(',')
        return cls(name, card_number, cvv, date, float(balance))

#Example
user_data = "Test User,1234567890123456,123,01/25,1000.0"
my_user_account = UserAccount.from_string(user_data)

print("Initial balance:", my_user_account.check_balance())
my_user_account.deposit(500)
print("Balance after deposit:", my_user_account.check_balance())

my_user_account.withdraw(200)
print("Balance after withdrawal:", my_user_account.check_balance())

print("Card number:", my_user_account.get_card_number())
print("CVV:", my_user_account.get_cvv())

# 2) Створити декілька(мінімум 4) класів які пов'язані з собою наслідуванням