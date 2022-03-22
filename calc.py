# Program makes a simple calculator

# This function adds two numbers


def add(x, y):
    return x + y

# This function subtracts two numbers


def subtract(x, y):
    return x - y

# This function multiplies two numbers


def multiply(x, y):
    return x * y

# This function divides two numbers


def divide(x, y):
    return x / y


print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter Choice (1/2/3/4): ")
