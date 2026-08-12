class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Книга: {self.title}, автор: {self.author},год: {self.year}")

    def is_old(self):
        now = 2026
        return (now - self.year) > 10


class Student:
    def __init__(self, name):
        self.name = name
        self._grades = []

    def add_grade(self, grade):
        self._grades.append(grade)

    def average(self):
        if self._grades:
            return sum(self._grades) / len(self._grades)
        else:
            return 0


# student = Student("Иван")
# # student.add_grade(4)

# # student.add_grade(5)
# # student.add_grade(5)
# print(student.average())


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0


# counter1 = Counter()
# counter2 = Counter()

# counter1.increment()
# counter1.increment()
# counter2.increment()


# print(counter1.value)
# print(counter2.value)
class Employee:
    company = "Яндекс"

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def info(self):
        print(f"Имя: {self.name}, Должность: {self.position}, Компания: {self.company}")


# class BankAccount:
#     bank_name = "Сбербанк"

#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Недостаточно средств")
#         else:
#             self.balance -= amount

#     def info(self):
#         print(f"Владелец: {self.owner},Баланс: {self.balance},Банк: {self.bank_name}")


class Library:
    total_books = 0  # атрибут класса

    def __init__(self, name):
        self.name = name  # атрибут экземпляра

    def add_books(self):
        Library.total_books += 1


# acc1 = BankAccount("Иван")  # баланс 0 по умолчанию
# acc2 = BankAccount("Мария", 500)
# print(acc2.info())


class Config:
    _saved = None

    def __new__(cls):
        if cls._saved is None:
            cls._saved = super().__new__(cls)
        return cls._saved

    def __init__(self):
        self.settings = {}


# c1 = Config()
# c1.settings["Theme"] = "Dark"
# c2 = Config()

# print(c1 is c2)
# print(c1)
# print(c2)


class AppLogger:
    _saved = None

    def __new__(cls):
        if cls._saved is None:
            cls._saved = super().__new__(cls)
            cls._saved._initialized = False
        return cls._saved

    def __init__(self):
        if not self._initialized:
            self.logs = []
            self._initialized = True

    def log(self, message):
        self.logs.append(message)


cl1 = AppLogger()
cl2 = AppLogger()

print(cl1, cl2)


class Account:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def deposit(self, amount):
        self._balance += amount

    def check_pin(self, pin):
        return self.__pin == pin


# acc = Account("Иван", 1000, "1234")

# print(acc.owner)  # Иван
# print(acc._balance)  # 1000
# acc.deposit(500)
# print(acc._balance)  # 1500
# print(acc.check_pin("1234"))  # True
# print(acc.check_pin("0000"))  # False


class BankAccount:
    def __init__(self, balance):
        self._balance = None
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Пополнение не может быть отрицательным")
        self._balance += amount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value


# acc = BankAccount(1000)  # OK
# print(acc.balance)  # 1000

# acc.deposit(500)  # OK
# print(acc.balance)  # 1500


# acc.balance = 2000  # OK — сеттер пропускает
# print(acc.balance)
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand}, {self.year}"


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def info(self):
        base = super().info()
        return f"{base}, дверей: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def info(self):
        base = super().info()
        if self.has_sidecar:
            return f"{base}, с коляской"
        return base


# car = Car("Toyota", 2020, doors=4)
# moto1 = Motorcycle("Harley", 2023, has_sidecar=True)
# moto2 = Motorcycle("Ducati", 2022, has_sidecar=False)

# print(car.info())     # Toyota, 2020, дверей: 4
# print(moto1.info())   # Harley, 2023, с коляской
# print(moto2.info())   # Ducati, 2022

# print(isinstance(car, Vehicle))     # True
# print(isinstance(moto1, Vehicle))   # True
# print(isinstance(car, Motorcycle))  # False
