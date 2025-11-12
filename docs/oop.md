# `self`, `__init__`, Class, Objects, Constructor, Methods & Attributes in Python

---

##  1. Class
A **class** is a blueprint for creating objects.  
It defines what attributes and methods an object will have.

```python
class Person:
    def __init__(self, name, age):
        self.n = name
        self.a = age
```
Here, Person is a class.

## 2. Objects
An object is an instance (real example) of a class. It is also something that is created from the class.

p1 = Person("Amisha", 21)
p1 is an object of the Person class.

Each object has its own copy of the class’s attributes.

##  3. Constructor – __init__()
__init__ is called automatically when an object is created.
It initializes the object’s attributes.

```python
def __init__(self, name, age):
    self.n = name
    self.a = age
```
When we run

```python
p1 = Person("Amisha", 21)
```
__init__ runs automatically.


self refers to p1.

"Amisha" → self.n

21 → self.a

## 4. What is self?
self means the object itself.
It is a reference to the current instance of the class.

It allows access to the object’s:

Attributes ➜ self.n, self.a

Methods ➜ self.display()

Without self, Python won’t know which object’s variables to use.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def display(self):
        print("Name:", self.n)
        print("Age:", self.a)

p1 = Person("Amisha", 21)
p1.display()
```
Output:

```python
Name: Amisha
Age: 21
```

p1.display()  internally means Person.display(p1)

self = p1

So self.n = p1.n, and self.a = p1.a

## 5. When is self used?
Self is used inside class methods to:

- Access instance variables

- Access other methods

- Differentiate instance variables from local ones

```python
def __init__(self, name):
    self.name = name  # instance variable
```

Without self, Python thinks name is just a local variable, not part of the object.

## 6. Why can’t we assign value to self?
We should not directly assign  to self like this:

```python
self = "text"  # Wrong
```
Because:

- self is automatically handled by Python.

- It points to the current object in memory.

- Changing it breaks the reference to the actual object.

So always we use self.attribute, not self = value.

## 7. Attributes and Methods
- Attributes are	Data/variables belonging to an object.
 Example;self.n, self.a
- Methods	are Functions inside a class. 
Example; def display(self):