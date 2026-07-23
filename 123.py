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


class BankAccount:
    bank_name = "Сбербанк"

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount

    def info(self):
        print(f"Владелец: {self.owner},Баланс: {self.balance},Банк {self.bank_name}")


class Library:
    total_books = 0  # атрибут класса

    def __init__(self, name):
        self.name = name  # атрибут экземпляра

    def add_books(self):
        Library.total_books += 1


lib1 = Library("Центральная")
lib2 = Library("Детская")

lib1.add_books()
lib1.add_books()
lib2.add_books()

print(lib1.total_books)  # 3
print(lib2.total_books)  # 3
print(Library.total_books)  # 3
