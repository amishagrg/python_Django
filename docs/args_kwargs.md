# args and kwargs in python
In Python, we use *args and **kwargs when we don’t know how many arguments a function will receive.

## args

*args allows a function to accept any number of positional arguments.

It collects them into a tuple.

```puython
def add_numbers(*args):
    print(args)   # args becomes a tuple
    return sum(args)

print(add_numbers(2, 4, 6))
```

```python
 Output:
(2, 4, 6)
12
```

## kwargs

**kwargs allows a function to accept any number of keyword arguments.

It collects them into a dictionary.

```python
def student_info(**kwargs):
    print(kwargs)  # kwargs becomes a dictionary
    for key, value in kwargs.items():
        print(f"{key} : {value}")

student_info(name="Amisha", age=21, course="Python")
```

```python
Output:
{'name': 'Amisha', 'age': 21, 'course': 'Python'}
name : Amisha
age : 21
course : Python
```