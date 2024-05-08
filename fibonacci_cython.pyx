# fibonacci_cython.pyx
cpdef int fib_recursive(int n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
