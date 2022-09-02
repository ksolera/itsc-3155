class Employee():
    def __init__(self, name, age,id,salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

emp2 = Employee("John, 23, 725554, 2000")

print(emp2.__dict__)