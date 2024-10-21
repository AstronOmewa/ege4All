from string import *
alf = '0123456789' + ascii_uppercase + ''.join([chr(x) for x in range(1000, 1500)])

def q_to_10(x, q):
    x1 = x[::-1]
    s = 0
    for i in range(len(x1)):
        s += alf.index(x1[i]) * q**i
    return s


def x_to_q(x,q):
    a = []
    if x == 0: return [0]
    while x > 0:
        a += [x%q]
        x //= q
    return a[::-1]

# ans = []
# m = 0
# for x in range(70000, 9, -1):
#     a = 5**2025 + 5**400 - x
#     k = f(a, 5)
#     k4 = k.count(4)
#     m = max(m, k4)
#     if k4 == m:
#         print(k4, x)


















                    
