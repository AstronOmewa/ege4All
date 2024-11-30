from itertools import *

def task2(table = '''''', results = [], vars = 'xyz', F = lambda x,y,z: x==y==z, unique = True):
    t = table.split(' ')
    spaces = len(t) - (t.count('1') + t.count('0'))
    
    for p in product([0,1],repeat=spaces):
        tx = []
        pc = 0
        for j in range(len(results)):
            f = []
            for i in range(len(t)//len(results)):
                if t[j*(len(results)-1)+i] in '01':
                    f.append(int(t[j*(len(results)-1)+i]))
                else:
                    f.append(p[pc])
                if t[j*(len(results)-1)+i] not in '01':
                    pc+=1
            tx.append(tuple(f))

        if unique:
            if len(set(tx))!=len(tx):
                continue
            
        for perm in permutations(vars,r=len(vars)):
            if [F(**dict(zip(perm,r))) for r in tx] == results:
                print(''.join(perm))    
        