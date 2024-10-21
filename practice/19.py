# def game(s=1,m=1,operand=">=",mn,steps=[],errors=False):
#     if not errors:
#         if eval(f'{s}{operand}{mn}'): return m%2==0
#         if m < 0: return 0

#         h = [game(eval(f'{s}{step}'),m-1,operand,mn,steps,errors) for step in steps]

#         if (m-1)%2==0: return any(h)
#         else: return any(h)
#     else: return all(h)

from functools import reduce

def f(s1,s2,m):
    if s1+s2 >= 178: return m%2==0
    if m < 0: return 0

    h = [f(s1+4,s2,m-1),f(s1,s2+3,m-1),f(s1*2,s2,m-1),f(s1,s2*3,m-1)]

    if (m-1)%2 == 0: return any(h)
    else: return any(h)

print('#19',min(s2 for s2 in range(1,157) if not f(21,s2,1) and f(21,s2,3)))
print('#20',sum(s2 for s2 in range(1,157) if not f(21,s2,1) and f(21,s2,3)))
print('#21',reduce(lambda x,y: x*y, [s2 for s2 in range(1,157) if not f(21,s2,1) and not f(21,s2,3) and f(21,s2,5)]))

# с ошибкой

