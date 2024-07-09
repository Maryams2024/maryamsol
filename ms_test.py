def fibonacci(n):
    """Generate Fibonacci series up to n terms."""
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

num_terms = 10  
fib_series = fibonacci(num_terms)
print(fib_series)



def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is the smallest prime number
    if num % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def smallest_10_primes():
    """Find the smallest 10 prime numbers."""
    primes = []
    num = 2  # smallest prime number
    while len(primes) < 10:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

prime_numbers = smallest_10_primes()
print("The smallest 10 prime numbers are:", prime_numbers)
