import time

def gcd(a:int, b:int) -> int:
    '''Greatest Common Divisor (using euclides algorithm)'''
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
    
def gcd_recursive(a:int, b:int) -> int:
    '''Greatest Common Divisor (using recursive euclides algorithm)'''
    if a == b:
        return a
    elif a > b:
        return gcd_recursive(a-b, b)
    else:
        return gcd_recursive(a, b-a)

def gcd_modulo(a: int, b: int) -> int:
    '''Greatest Common Divisor (using modulo)'''
    while b:
        c = a % b
        a = b
        b = c
    return a

test_values = [
    (315, 504),
    (1230, 528),
    (28, 8),
    (12, 18),
    (100, 1)
]

start_time = time.time()
for i in range(1,1000):
    for a,b in test_values:
        gcd(a,b)
end_time = time.time()
print("Czas wykonania dla funkcji gcd 5000 razy:", (end_time-start_time) * 1000, "ms")


start_time = time.time()
for i in range(1,1000):
    for a,b in test_values:
        gcd_modulo(a,b)
end_time = time.time()
print("Czas wykonania dla funkcji gcd_modulo 5000 razy:", (end_time-start_time) * 1000, "ms")


start_time = time.time()
for i in range(1,1000):
    for a,b in test_values:
        gcd_recursive(a,b)
end_time = time.time()
print("Czas wykonania dla funkcji gcd_recursive 5000 razy:", (end_time-start_time) * 1000, "ms")


for a,b in test_values:
        gcd_modulo(a,b)
#63
#6
#4
#6
#1

# Czas wykonania dla funkcji gcd 5000 razy: 8.148431777954102 ms
# Czas wykonania dla funkcji gcd_modulo 5000 razy: 1.9202232360839844 ms
# Czas wykonania dla funkcji gcd_recursive 5000 razy: RecursionError: maximum recursion depth exceeded
# Czas wykonania dla funkcji gcd_recursive 5000 razy: (14.826297760009766 ms dla testowej wartosci: 100, 1)