# module_4_functions_&_modules_in_python

Python Assignment 3 — Functions & Modules in Python

This repository contains solutions for Module 4: Functions & Modules in Python.
It includes two tasks that demonstrate working with functions (including recursion/loops) and using Python's built-in math module.

# Tasks Overview
Task 1 — Calculate Factorial Using a Function

Problem Statement
Create a Python program that:

Defines a function named factorial that accepts a non-negative integer and computes its factorial (you may use a loop or recursion).

Returns the calculated factorial.

Calls the function with a sample number and prints the result.

Expected Example
If the function is called with 5, the output should be:

Factorial of 5 is: 120


File: task1_calculate_factorial.py

Task 2 — Using the math Module for Calculations

Problem Statement
Create a Python program that:

Prompts the user for a number.

Uses the math module to compute:

Square root of the number (math.sqrt)

Natural logarithm — log base e (math.log)

Sine of the number (in radians) (math.sin)

Prints the calculated results.

Expected Example
If the user inputs 25, the output should be similar to:

Input number: 25
Square root: 5.0
Natural logarithm (ln): 3.2188758248682006
Sine (radians): -0.13235175009777303


File: task2_math_modules.py

# How to Run

Clone the repository:

git clone https://github.com/nsroyale9740/module_4_functions_-_modules_in_python.git


Change into the project directory:

cd module_4_functions_-_modules_in_python


Run each script:

python task1_calculate_factorial.py
python task2_math_modules.py

Use python3 instead of python if your system requires that.

# Concepts Covered

Function definition and invocation

Recursion and/or iterative loops

Return values from functions

Using Python standard library modules (math)

Input validation and error handling

Formatted output

# Validation & Error Handling

Task 1 (factorial):

Ensure the input is a non-negative integer.

Handle invalid inputs negative number with friendly error messages.


Task 2 (math module):

Validate the input is numeric.

For math.log, ensure the number is > 0 (log undefined for non-positive values); show a clear error if the user enters non-positive values.

## Repository Structure

module_4_functions_-_modules_in_python/
│
├── task1_calculate_factorial.py         # Task 1: factorial function (loop or recursion)
├── task2_math_modules.py       # Task 2: uses math module for sqrt, log, sin
└── README.md                  # This documentation

# Notes & Tips

Test both scripts with multiple inputs (edge cases like 0, 1, negative numbers, non-integer) before submitting.


Author

Name: Naveen
Course: Functions & Modules in Python — Module 4 Assignment
GitHub: https://github.com/nsroyale9740/module_4_functions_-_modules_in_python.git