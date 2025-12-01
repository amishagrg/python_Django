class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name        
        self.age = age          
        self.salary = salary 

    def increaseSalary(self):
        self.salary = self.salary + (self.salary * 0.20)

    # to print current salary
    def printSalary(self):
        print(f"{self.name} current salary is: {self.salary}")


a = Employee("Ram", 21, 30000)
b = Employee("Sita", 20, 20000 )

# current salary
a.printSalary()
b.printSalary()

a.increaseSalary()
b.increaseSalary()

# updated salary
a.printSalary()  
b.printSalary()
