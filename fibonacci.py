# fibonacci.py

def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
