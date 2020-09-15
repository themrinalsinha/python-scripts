# == V1 =========================================
def gcd(a: int, b: int):
    """
    computes greatest common divisor
    """

    while b:
        a, b = b, a % b
    return a

print(gcd(27, 36))       # 9
print(gcd(2.7, 3.6))     # 4.4.....
# print(gcd('2.7', '3.6')) # error - TypeError
# so, we can pass these type hints, but they actually dont
# do anything...


# == V2 =========================================
def gcd(a, b):
    """
    computes greatest common divisor
    """

    # asserting and checking if the value is integer
    assert isinstance(a, int), 'Expected Int'
    assert isinstance(b, int), 'Excepted Int'

    while b:
        a, b = b, a % b
    return a
