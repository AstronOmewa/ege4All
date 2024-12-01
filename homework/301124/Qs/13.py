ans = '\n'

from math import sqrt
from functools import reduce
def cnt_d(n):
    m = n
    pairs = []
    
    i = 2
    for i in range(2,int(sqrt(n))+1):
        if m%i == 0:
            pairs.append((i,0))

    for i in pairs:
        while m%i[0] == 0:
            i = (i[0], i[1]+1)
            m/=i[0]

    return reduce(lambda x,y: x*y, [(p[1]+1) for p in pairs])

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
