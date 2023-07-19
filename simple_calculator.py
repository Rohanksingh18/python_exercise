
# Exercise : Simple Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print("Sum:", sum_result)

# Subtraction
difference = num1 - num2
print("Difference:", difference)

# Multiplication
product = num1 * num2
print("Product:", product)

# Division
if num2 != 0:
    division_result = num1 / num2
    print("Division:", division_result)
else:
    print("Cannot divide by zero.")
