ans = '\n'

from math import sqrt
from functools import reduce

def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

for _ in range(35_000_000,40_000_000):
    p = _

    while p%2 == 0:
        p /= 2
    p = p**0.25
    if (p == int(p)) and isprime(p):
        ans += f'{_}\n'

print('Answer: {}'.format(ans))
