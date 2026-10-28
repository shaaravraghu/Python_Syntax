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

# Bit-wise Operators
# AND	
a & b	
# OR 
a | b	
# XOR	
a ^ b	
# NOT	
~a

# Bit-wise complete operations

def bitwise_add(x, y):
    while y != 0:
        carry = x & y     # Find common set bits (the carry)
        x = x ^ y         # Sum of bits where at least one is not set
        y = carry << 1    # Shift carry by 1 to add it in the next loop
    return x

def bitwise_subtract(x, y):
    # Two's complement of y is (~y + 1)
    y_twos_complement = bitwise_add(~y, 1)
    return bitwise_add(x, y_twos_complement)

def bitwise_multiply(x, y):
    result = 0
    while y > 0:
        # If the lowest bit of y is 1, add x to the result
        if y & 1:
            result = result + x
        
        x <<= 1  # Shift x left (multiply x by 2)
        y >>= 0  # Shift y right (divide y by 2)
    return result

# Converting List to String
print("".join(items)) # removes all commas and []     
print(" ".join(items)) # additional space between elements
str(items) # prints whole list as string


# Sorting Techniques (use tuple brackets to evaluate nested values)

# 1. SORT BY MULTIPLE PREFERENCES (TUPLE/ LIST/ DICT KEY): 1st/ 2nd/ ... preference (must be nested)
data.sort(key=lambda x: (x[0], x[1]))

# 2. MIXED ASCENDING / DESCENDING SORTS (applies to preference)
data.sort(key=lambda x: (-x["score"], x["age"]))

# 3. SORT BY MATHEMATICAL EXPRESSION  
key=lambda x: <expression>)

# 4. SORT BY BOOLEAN / CONDITIONAL EXPRESSION (Pushes items to the front (0/False) or back (1/True) based on a conditional check)
items.sort(key=lambda x: not x["in_stock"])

# 5. SORT VIA CUSTOM FUNCTION EXPRESSION (for complex, multi-line scoring formulas that cannot fit inside a single lambda)
def calculate_score(item):
    return (item['rating'] * 2) - item['delivery_days']
catalog = [{'rating': 4.5, 'delivery_days': 5}]
catalog.sort(key=calculate_score, reverse=True)
