

# Exercise: (Area of a Circle) Functions in Python, which are reusable blocks of code that perform a specific task.
import math


def calculate_circle_area(radius):
    return math.pi * radius ** 2


# Get radius from the user
radius = float(input("Enter the radius of the circle: "))

# Call the function and calculate the area
area = calculate_circle_area(radius)

# Display the result
print("The area of the circle is:", area)
