from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_annual_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12


class Contractor(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_annual_salary(self):
        return self.hourly_rate * self.hours_worked


employees = [
    FullTimeEmployee("Alice", 1500),
    FullTimeEmployee("Chloe", 2000),
    Contractor("Quoc", 15, 1800),
    Contractor("Phat", 20, 1500),
]

for emp in employees:
    print(f"{emp.name}: {emp.calculate_annual_salary()} USD/year")