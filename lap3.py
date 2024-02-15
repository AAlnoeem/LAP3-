
# 1-Create an empty dictionary to store employee salaries
employee_salaries = {}

# Iterate indefinitely until the user enters 'no'
while True:
    # Prompt the user to enter the name of the employee or 'no' to stop
    name = input("Enter the name of the employee (or 'no' to stop): ")
    
    # Check if the user entered 'no', if so, exit the loop
    if name.lower() == 'no':
        break
    
    # Prompt the user to enter the salary of the employee
    salary = float(input("Enter the salary of the employee: "))
    
    # Store the name and salary of the employee in the dictionary
    employee_salaries[name] = salary

# Print the dictionary containing the employee salaries
print("\nEmployee salaries stored in dictionary:")
print(employee_salaries)


# 2- Initialize an empty list to store user inputs
numbers = []

# Ask the user to input 10 values into the list
for i in range(10):
    value = float(input(f"Enter value {i+1}: "))
    numbers.append(value)

#3- Initialize a variable to store the maximum number found
max_number = numbers[0]

# Iterate through the list to find the largest number
for number in numbers:
    if number > max_number:
        max_number = number

# Display the largest number
print("The largest number in the list is:", max_number)

# 4- Prompt the user to input a Celsius temperature
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula F = (9/5) * C + 32
fahrenheit = (9/5) * celsius + 32

# Output the equivalent temperature in Fahrenheit
print("Equivalent temperature in Fahrenheit:", fahrenheit)

# 5-Prompt the user to input a number
number = int(input("Enter a number: "))

# Print the multiplication table for the entered number up to 10
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 6- Define a decorator function that repeats the execution of the decorated function
def repeat_hello(num_repetitions):
    # Define the decorator that takes the number of repetitions as an argument
    def decorator(func):
        # Define the wrapper function that will call the original function multiple times
        def wrapper():
            # Repeat the call to the original function 'num_repetitions' times
            for _ in range(num_repetitions):
                func()
        return wrapper  # Return the wrapper function
    return decorator  # Return the decorator function

# Prompt the user to enter the number of repetitions
x = int(input("Enter a number of repetitions: "))

# Decorate the 'hello' function with the specified number of repetitions
@repeat_hello(x)
def hello():
    print('Hello')  # Define the original function to be repeated

hello()  # Call the decorated 'hello' function
