class car:
    def __init__(self, brand, color, velocity):
        self.brand = brand
        self.color = color
        self.velocidad = velocity

    def move(self):
        print(f"The car is fast")

    def describe(self):
        print(f"The car is slow {self.velocidad} km/h")

#Create multiple instances of the Car class
#Instance 1
table1 = car("Toyota", "Red", 120)
#Instance 2
table2 = car("Honda", "Blue", 100)
print(table1.brand)
print(table2.brand)
table1.describe()
table2.describe()

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def check_balance(self):
        print(f"Saldo actual: ${self.__balance}")

account1 = BankAccount("Raúl Pérez", 5000)
account2 = BankAccount("Joel López", 3000)

#Raúl Pérez
print(account1.holder)
account1.check_balance()
account1.deposit(1000)
account1.withdraw(2000)
account1.check_balance()

print("------------------")

#Joel López
print(account2.holder)
account2.check_balance()
account2.deposit(500)
account2.withdraw(1000)
account2.check_balance()