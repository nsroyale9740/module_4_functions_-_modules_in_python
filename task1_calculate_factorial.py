n = int(input("Enter a number to calculate its factorial: "))

'''
This script calculates the factorial of a given number using different methods:
1. For loop
2. While loop
3. Recursion
'''

#with for loop

# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         factorial = 1
#         for i in range(1, n + 1):
#             factorial *= i
#         return factorial

#with while loop

# def factorial(n):
#     factorial = 1
#     while n > 1:
#         if n < 0:
#             print(f"Factorial is not defined for negative numbers")
#             return None
#         elif n == 0 or n == 1:
#             print(f"The factorial of {n} is: 1")
#             return 1
#         else:
#             factorial *= n
#             n -= 1
#     return factorial

#with recursion

def factorial(num):
    if num < 0:
        return "factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(f"The factorial of {n} is: {factorial(n)}")
