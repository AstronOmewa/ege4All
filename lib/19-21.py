def f(s, m, p):
    if s >= 121: return m%2 == 0
    if m < 0: return 0

    h = []

    if len(p) < 2: h += [f(s+2, m-1, p+'1'),f(s+5, m-1, p+'2'),f(s+12, m-1, p+'3'),f(s*2, m-1, p+'4')]
    else:
        if p[-2] != '1': h += [f(s+2,m-1,p+'1')]
        if p[-2] != '2': h += [f(s+5,m-1,p+'2')]
        if p[-2] != '3': h += [f(s+12,m-1,p+'3')]
        if p[-2] != '4': h += [f(s*2,m-1,p+'4')]
    
    if (m-1)%2 == 0:
        return any(h)
    else:
        return all(h)

print('#19',)
print('#20',min(s for s in range(1,122) if f(s,3,'') and not f(s,1,'')))
print('#21',[s for s in range(1,122) if not f(s,2,'') and not f(s,4,'') and f(s,6,'')])