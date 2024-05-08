# main.py
import fibonacci
import fibonacci_cython  # Import the Cython module
import time

def main():
    n = 35
    
    # Without Cython
    start = time.time()
    fib_rec = fibonacci.fib_recursive(n)
    end = time.time()
    print(f"Recursive Fibonacci (Python): {fib_rec}, Time taken: {end - start} seconds")
    
    # With Cython
    start = time.time()
    fib_rec_cython = fibonacci_cython.fib_recursive(n)
    end = time.time()
    print(f"Recursive Fibonacci (Cython): {fib_rec_cython}, Time taken: {end - start} seconds")

if __name__ == "__main__":
    main()
