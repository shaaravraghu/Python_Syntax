# Prime Numbers
from sympy import isprime, primerange, prime
# 1. Instantly check if a huge number is prime
print(isprime(32416190071))  # True
# 2. Get a range of primes (like a pre-stored slice)
primes_list = list(primerange(100, 150)) # [a, b): range
# 3. Get the exact n-th prime number
print(prime(100000))  # 1,299,709 (The 100,000th prime number)

# Common Elements in 2 strings
set(str1).isdisjoint(str2)
