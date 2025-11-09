# hw

# Q1) In python we take input using the input() function
# input() always returns string so we need to convert it to other types if needed
# a) String input
name= input("Enter your name: ")
print("Your name is:", name)

# b) Integer input
age= int(input("Enter your age: "))
print("Your age is:", age)

# c) Float input
salary= float(input("Enter your monthly salary: "))
print("Your salary is:", salary)


# Q2) 
# a) Funtion with arguments and return value
def divide_number(x,y):
    if y != 0:
        return x/y
    else:
        return "Division by 0 is not allowed"
# b) Function with no arguments and no return value
def add_numbers():
    a= 3
    b= 7
    finalSum= a+b
    print("Sum:", finalSum)
# c) Function with arguments but no return value
def subtract_numbers(x,y):
    finalResult= x - y
    print("Difference:", finalResult)
# d) Function with no arguments but returns a value
def multiply_numbers():
    a= 4
    b= 5
    return a*b
    
# calling the function
add_numbers()
print("Quotient:", divide_number(10, 2))
subtract_numbers(10,5)
print("Multiplication:", multiply_numbers())

# e) Funtion with arguments and return value
def modulus(x,y):
    return x%y

result= modulus(10,3)
print("Remainder:", result)


# Q3) nested for loop herera bubble sort algorithm
# A nested for loop means a for loop inside another for loop
# The outer loop runs first, and for each time the outer loop runs once, the inner loop runs completely.
# The Bubble Sort algorithm is one of the simplest sorting methods used to arrange a list of elements (like numbers) in ascending or descending order.
numbers = [5, 3, 8, 4]

for i in range(3):             # Repeat 3 times (since 4 numbers)
    for j in range(3 - i):     # Compare pairs
        if numbers[j] > numbers[j + 1]:
            # Swaping if in wrong order
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted list:", numbers)


# Q4) pattern
noOfRows= 4
for i in range(1, noOfRows + 1): # loop runs 4 times
    print("*" * i)


# another pattern
noOfRows= 4
for i in range(1, noOfRows + 1):
    spaces = " " * (noOfRows - i)
    stars = "* " * i
    print(spaces + stars)