README.md

# Fibonacci Calculator

This Python project provides functions for calculating Fibonacci numbers both recursively and iteratively. Additionally, it includes a Cython implementation for accelerating the recursive Fibonacci calculation.

## Modules:

### 1. fibonacci.py

This module contains functions for calculating Fibonacci numbers.

- `fib_recursive(n)`: Calculates the nth Fibonacci number recursively.
- `fib_iterative(n)`: Calculates the nth Fibonacci number iteratively.

### 2. fibonacci_cython.pyx

This Cython module provides an accelerated implementation of the recursive Fibonacci calculation.

- `fib_recursive(n)`: Calculates the nth Fibonacci number recursively using Cython.

## Usage:

1. **Importing the Modules**:
   
   ```python
   import fibonacci
   import fibonacci_cython
2. Calculating Fibonacci Numbers:
    To calculate the nth Fibonacci number recursively
      result_recursive = fibonacci.fib_recursive(n)
    To calculate the nth Fibonacci number iteratively
      result_iterative = fibonacci.fib_iterative(n)
    To calculate the nth Fibonacci number recursively using Cython
      result_cython = fibonacci_cython.fib_recursive(n)


3. Example:
import fibonacci
import fibonacci_cython

# Calculate the 10th Fibonacci number recursively
result_recursive = fibonacci.fib_recursive(10)
print("Recursive Fibonacci (Python):", result_recursive)  # Output: 55

# Calculate the 10th Fibonacci number iteratively
result_iterative = fibonacci.fib_iterative(10)
print("Iterative Fibonacci (Python):", result_iterative)  # Output: 55

# Calculate the 10th Fibonacci number recursively using Cython
result_cython = fibonacci_cython.fib_recursive(10)
print("Recursive Fibonacci (Cython):", result_cython)  # Output: 55
