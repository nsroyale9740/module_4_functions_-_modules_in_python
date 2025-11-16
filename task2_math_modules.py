import math
num = int(input("Enter a number: "))

def calculate_square_root(num):
    if num <= 0:
        return f"Square root is not defined for {num} or negative numbers"
    return math.sqrt(num)

def calculate_logarithm(num):
    if num <= 0:
        return "Logarithm is not defined for non-positive numbers"
    return math.log(num)

def calculate_sine(num):
        return math.sin(num)

# calculate_square_root(num)
# calculate_logarithm(num)
# calculate_sine(num)

print(f"The square root of {num} is: {calculate_square_root(num)}")
print(f"The natural logarithm of {num} is: {calculate_logarithm(num)}")
print(f"The sine of {num} is: {calculate_sine(num)}")