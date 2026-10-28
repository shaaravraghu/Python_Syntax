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

# Initialising a List
# Constant Characters
a = [1]*n
a = [1 for _ in range(n)]
# Incremental Characters
a = [x for x in range(n)]
# if condition on range
a = [x for x in range(n) if (<condition>)] # if alwyas at the end
# if-else condition on range
a = [x if (<condition>) else alternate_val for x in range(n)] # if alwyas at the end
# elif and for-else cannot be used here

# Binary Representation
# bin
print(bin(number))        # Output: '0b_'
# Without prefix
print(bin(number)[2:])    # Output: '_'
# Using format()
print(format(number, 'b'))  # Output: '_'
# Using f-string 
print(f"{number:b}")        # Output: '_'
