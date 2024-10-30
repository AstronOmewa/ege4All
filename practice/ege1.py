# graph = 'АБ АВ БВ БГ ВГ ВД ГВ ГД ДЕ'.split()
# table = '256 15 4 356 1246 145'.split()

# from itertools import permutations
# print('1 2 3 4 5 6')
# for p in permutations('АБВГДЕ'):
#     # print(*[(str(p.index(c2)+1),table[p.index(c1)]) for c1,c2 in graph],end = '\n')
#     if all(str(p.index(c1)+1) in table[p.index(c2)] for c1,c2 in graph):
#         print(*p)
#         break

###

# from itertools import *
# def f(x,y,z,w):
#     return (y <= z) and not((y or w) <= (z and x))

# for a1,a2,a3,a4,a5 in product([0,1],repeat=5):
#     t = [
#         (1, 1,a1, 1),
#         (a2,1, 1,a3),
#         (1, 1,a4,a5)
#         ]
#     if len(t)!=len(set(t)): continue
#     for p in permutations('xyzw',r=4):
#         if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
#             print(''.join(p))

# # for n in range(1,100_000_000):
#     r = bin(n)[2:]
#     if n%2 == 0:
#         r = '10' + r
#     else:
#         r = '1' + r + '01'
    
#     r = int(r,2)

#     if n == 5:
#         print(r)
#     if r > 516:
#         print(n)
#         break

# from math import *

# for n in range(20000):
#     video_size = 900*600*ceil(log2(1024))*(1-0.9)*n #bits
#     q = 800*2**13
#     if q >= video_size:
#         print(n)


# alf = 'АМУХ'

# from itertools import product
# a = []
# for p in product(alf,repeat=4):
#     a.append(''.join(p))

# print(a.index('ХУХХ')+1)



# c = 0
# with open('practice/t9.txt','r+') as f:
#     a = [list(map(int,x.replace('\n','').split(' '))) for x in f.readlines()]
#     # print(a)
#     for i in range(len(a)):
        
#         if (len(a[i])==len(set(a[i]))) and 2*( sum(a[i])-(min(a[i])+max(a[i])) ) >= 3*( min(a[i])+max(a[i]) ):
#             c+=1

# print(c)

# from ipaddress import *

# ip1 = '98.162.71.150'
# ip2 = '98.162.71.140'

# for m in range(24,33):
#     mask = '1' * m + '0'*(32 - m)
#     net = [str(ip) for ip in ip_network(f'{ip1}/{m}', 0)]

#     if ip2 in net:
#         print(m)


# for x in range(9):
#     if (int(f'88{x}4{x}', 9) + int(f'7{x}344', 9))%67 == 0:
#         print((int(f'88{x}4{x}', 9) + int(f'7{x}344', 9))//67)

# def f(n):
#     if n<=2:
#         return 1
#     else:
#         return 2*f(n-1)+f(n-2)
    
# print(f(7))

# def f(x,y):
#     if x>y:
#         return 0
#     if x == 33:
#         return 0
#     if x == y:
#         return 1
#     return f(x+1,y)+f(x*2,y)+f(x*3,y)

# print(f(3,15)*f(15,50))


print([(2**x%7,5**x%7) for x in range(1,10)]) # 2**n==2**(n mod 3), 5**n == 5**(n mod 6)
# 2**555 == 2**(555 mod 3)