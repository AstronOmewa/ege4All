# def f(x,y,z,w):
#     return not(not(x <= (not w)) and z) and not(w <= z) and (x <= (not z))

# from itertools import *
# cntr = 0

# s = set()

# for a1, a2, a3, a4, a5 in product([0,1], repeat = 5):
#     t = [
#         (1, 0, a1, 0),
#         (1, 0, a2, a3),
#         (a4,1, a5, 1)
#     ]
#     if len(t) != len(set(t)): continue

#     for p in permutations('xyzw'):
#         if [f(**dict(zip(p, r))) for r in t] == [1,0,0]:
#             s.add(''.join(p))

# print(len(s),s)



# maxsum = 0
# from random import shuffle

# for n in range(0,21):
#     # for m in range(0,21):
        
#         for i in range(200):
#             s = '0'*n+'1'*(20-n)
            
#             s = list(s)
            
#             shuffle(s)
#             s = ''.join(s)+'<'
#             if '000' in s or '111' in s: continue

#             while '0<' in s or '1<' in s:
#                 if '11<' in s: s = s.replace('11<','<3',1)
#                 if '10<' in s: s = s.replace('10<','<2',1)
#                 if '00<' in s: s = s.replace('00<','<0',1)
#                 if '01<' in s: s = s.replace('01<','<1',1)
            
#             maxsum = max(maxsum, sum(int(x) for x in s if x!= '<'))

# print(maxsum)



# from ipaddress import ip_network

# ipn = ip_network('123.222.111.192/255.255.255.192')

# ans = len([x for x in ipn if bin(int(str(x).split('.')[-1]))[2:].count('1')%3!=0])
# print(ans)


# def f(x, A):
#     return not(((x|41) == 0) or ((x&128) != 0)) and ((x&A) == 0) and (((x|A) == 0) or ((x&A) == 0))

# ans = set()

# for A in range(1,100000):
#     if all([f(x, A)==1 for x in range(10,100)]):
#         ans.add(A)
    
# print(min(ans))


# cnt,maxsum = 0,0

# with open('progress_check\\02-12-24\\data\\17 (3).txt') as f:
#     a = [int(x) for x in f.readlines()]

#     max47 = max([x for x in a if x%100 == 47])

#     for i in range(len(a)-4):
#         if sum(a[i+k]>1000 for k in range(4))==2 and sum(a[i+k] for k in range(4))<=max47:
#             cnt += 1
#             maxsum = max(maxsum, sum(a[i+k] for k in range(4)))

# print(cnt,maxsum)



# def f(s, m):
#     if s > 77: return m%2 == 1
#     if s >= 55 and s <=77: return m%2 == 0

#     if m == 0: return 0

#     h = [f(s+3, m-1), f(s*2, m-1), f(s*3, m-1)]

#     if (m-1)%2 == 0:
#         return any(h)
#     else:
#         return all(h)
    
# print(f'19: {len([s for s in range(55) if f(s,2) and not f(s,1)])}')
# print(f'20: {min([s for s in range(55) if f(s,3) and not f(s,1)])} {len([s for s in range(55) if f(s,3) and not f(s,1)])}')
# print(f'19: {max([s for s in range(55) if f(s,4) and not f(s,2)])}')



# from fnmatch import fnmatch
# from math import sqrt

# def mindiv(k):
#     for i in range(2,int(sqrt(k))+1):
#         if k%i == 0:
#             if i == k//i:
#                 return i
#             else:
#                 return i+k//i
#     return 0

# ans = set()

# for a in ['']+[str(x) for x in range(10)]:
#     for b in ['']+[str(x) for x in range(10)]:
#         for c in [str(x) for x in range(10)]:
#             k = int(f'51{a}{b}2{c}34')
#             if (2+k//2)%117 == 0 and k<10**8:
#                 ans.add((k,2+k//2))

# print(*sorted(ans),sep = '\n')