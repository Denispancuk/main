class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        print(f"Імя: {self.name}, Зарплата: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def describe(self):
        print(f"Імя: {self.name}, Зарплата: {self.salary}, Департамент: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def describe(self):
        print(f"Імя: {self.name}, Зарплата: {self.salary}, Мова Програмування: {self.programming_language}")

manager1 = Manager("Aліса", 120000, "Продажі")
developer1 = Developer("Назар", 90000, "Python")
developer2 = Developer("Кирил", 95000, "JavaScript")

manager1.describe()
developer1.describe()
developer2.describe()