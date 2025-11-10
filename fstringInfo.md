## Python F-Strings (Formatted String Literals)

### What is an F-String?

Python introduced f-strings to make string formatting easier. With f-strings we can directly embed variables and expressions inside strings using curly braces.
To use f-strings, simply prefix a string with f and place variables or expressions inside {}.

---

###  Basic Syntax

```python
name = "Amisha"
age = 21
print(f"My name is {name}, and I am {age} years old.")
```

> We should always prefix our string with either **f** or **F**.

---

###  Why F-Strings is used?

- Easier to read and write  
- Faster than older formatting methods (% formatting or str.format())  
- Supports expressions, and functions

---
### Everything we can do with f-strings in python

### 1. Insert variables
We can directly include variables inside {}.
```python
name= "Amisha"
print(f"Hello {name}")
```

### 2. Performing Calculations
We can perform operations inside the curly braces.

```python
x = 20
y = 10
print(f"The sum of {x} and {y} is {x + y}.")
```

### 3. Calling Functions Inside F-Strings

We can even call functions inside {}.

```python
def add(a,b):
    return a+b

x=5
y=3
print(f"The sum of {x} and {y} is {add(x, y)}.")
```

---

### 4. Formatting Numbers
We can format floats, percentages and large numbers.

#### i. Decimal Places
```python
pi = 3.14159265
print(f"Value of pi: {pi:.2f}")
```
Output:
```
Value of pi: 3.14
```

#### ii. Adding Commas
```python
num = 1000000
print(f"{num:,}")
```
Output:
```
1,000,000
```

#### iii. Percentage
```python
score = 0.675
print(f"Success rate: {score:.2%}")
```
Output:
```
Success rate: 67.50%
```

---

### 5. Using Dictionaries and Lists

We can directly reference elements from collections.

```python
person = {"name": "Amisha", "age": 21}
print(f"{person['name']} is {person['age']} years old.")
```

---

### 6. Using Multi-line F-Strings

F-strings can span multiple lines using triple quotes.

```python
name = "Amisha"
age = 21
bio = f"""
Name: {name}
Age: {age}
Status: {'Student'}
"""
print(bio)
```
---

### Advantages of F-Strings

- Clear and readable syntax  
- Faster performance  
- Works with functions and data structures   








