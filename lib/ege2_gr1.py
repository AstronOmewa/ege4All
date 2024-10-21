'''
(№ 7642) (Демо-2025) Логическая функция F задаётся выражением ((w → y) → x) ˅ ¬z. На рисунке
приведён частично заполненный фрагмент таблицы истинности функции F, содержащий
неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F соответствует
каждая из переменных x, y, z, w.
 В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы.
 Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
'''
def f(x,y,z,w):
    return ((w <= y) <= x) or not z

##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                if not f(x,y,z,w):
##                    print(x, y, z, w)

from itertools import *

spermutations = permutations

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat = 7):
    t = [(a1, a2, 1, a3),
         (a4, 0, a5, a6),
         (a7, 1, 0, 0)]
    if len(set(t)) != len(t): continue
    for p in spermutations('xyzw'):
        if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
            print(*p)

from itertools import *

def task2(table = '''''', results = [0,0,0], vars = 'xyzw', F = lambda x,y,z,w: x==y==z==w, unique = True):
    t = table.split(' ')
    print(t)
    spaces = 0
    indexes = []
    for x in range(len(t)):
        if t[x] == '_':
            spaces+=1
            indexes.append((x//len(results),x%len(results)))
    
    
    for p in product([0,1],repeat=spaces):
        tx = [

        ]
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
        print(tx,sep = '\n')

        # for prm in spermutations(vars,r=len(vars.split())):
        #     if [F(**dict(zip(prm,r))) for r in tx] == results:
        #         print(*prm)    
        
        
print(task2("_ _ 1 _ 0 _ _ 1 1 _ _ 1",[0,0,0,0],vars='xyzw',F = lambda x,y,z,w: x == y == (not z) == (not w)))