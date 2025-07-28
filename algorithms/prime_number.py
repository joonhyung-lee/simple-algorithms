import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@time_it
def is_prime(n: int) -> bool:
    """
        Check if a number is prime.
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

@time_it
def is_prime_optimized(n: int) -> bool:
    """
        Check if a number is prime.
    """
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("==== Get Prime Number ====")
print(is_prime(2))
print(is_prime(901256437))

print("==== Get Prime Number (Optimized) ====")
print(is_prime_optimized(2))
print(is_prime_optimized(901256437))

"""
Result:
==== Get Prime Number ====
Time taken: 0.000001 seconds
True
Time taken: 22.205987 seconds
True
==== Get Prime Number (Optimized) ====
Time taken: 0.000009 seconds
True
Time taken: 0.000800 seconds
True
"""