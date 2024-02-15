employee_salaries = {}

while True:
    name = input("Enter the name of the employee (or 'no' to stop): ")
    if name.lower() == 'no':
        break
    
    salary = float(input("Enter the salary of the employee: "))
    employee_salaries[name] = salary

print("\nEmployee salaries stored in dictionary:")
print(employee_salaries)

# Initialize an empty list to store user inputs
numbers = []

# Ask the user to input 10 values into the list
for i in range(10):
    value = float(input(f"Enter value {i+1}: "))
    numbers.append(value)

# Initialize a variable to store the maximum number found
max_number = numbers[0]

# Iterate through the list to find the largest number
for number in numbers:
    if number > max_number:
        max_number = number

# Display the largest number
print("The largest number in the list is:", max_number)

# Prompt the user to input a Celsius temperature
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula F = (9/5) * C + 32
fahrenheit = (9/5) * celsius + 32

# Output the equivalent temperature in Fahrenheit
print("Equivalent temperature in Fahrenheit:", fahrenheit)

# Prompt the user to input a number
number = int(input("Enter a number: "))

# Print the multiplication table for the entered number up to 10
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

    
def repeat_hello(num_repetitions):
    def decorator(func):
        def wrapper():
            for _ in range(num_repetitions):
                func()
        return wrapper
    return decorator

x = int(input("Enter a number of repetitions: "))

@repeat_hello(x)
def hello():
    print('Hello')

hello()
