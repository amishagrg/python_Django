# My Python CSV Project

This project writes and filters student data using CSV files.

## Files
- `csv_write.py` → writes records of 10 students.
- `csv_high_scorers.py` → filters students with marks > 60.

## Access Specifiers in Python (Public, Protected, Private)

Python uses naming conventions to control access to class members (variables and methods).

### Access modifiers
Python does not have true access modifiers as the language trusts the programmer to follow rules responsibly instead of forcing them through restrictions.

So instead of keywords like public, protected, or private, Python uses underscore conventions:

### Public Members (default)

Accessible anywhere in the program.

Defined normally without underscore before the name.

```python
class Student:
    def __init__(self, name):
        self.name = name  # public variable

s = Student("Amisha")
print(s.name)  # accessible
```

### Protected Members

Indicated by a single underscore _variable.

Should not be accessed outside the class directly (by convention).

Still accessible outside the class, but intended for subclass use.

```python
class Student:
    def __init__(self, name):
        self._name = name  # protected by convention

class Derived(Student):
    def show(self):
        print("Name:", self._name)

s = Derived("Riya")
s.show()        # Allowed
print(s._name)  # Works, but not recommended
```

So _variable means: We can access this, but please don’t unless necessary.

### Private Members

Indicated by double underscore __variable.

Cannot be accessed directly outside the class.

Interpreter changes its name internally (name mangling) to make it hard to access

```python
class Student:
    def __init__(self, name):
        self.__name = name  # private variable

    def display(self):
        print("Student name:", self.__name)

s = Student("Sam")
s.display()          #  works
# print(s.__name)    #  error
print(s._Student__name)  #  accessed using name mangling
```

###  What is Recursion?

Recursion is a process in which a function calls itself to solve smaller instances of a problem.
Recursion= function calling itself

### Example: Factorial using Recursion
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

print(factorial(5))  # Output: 120
```

Explanation:

Each call to factorial() reduces n by 1.

When n reaches 1, recursion stops.

The results are then multiplied as the stack unwinds.

### Why Use Recursion?

Makes code shorter and elegant
Useful for problems like factorial, Fibonacci, tree traversal, etc.
Too many recursive calls may cause a RecursionError.