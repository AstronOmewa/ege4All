ans = [0]

def trian(a, b, c):
    if (a+b > c) and (a+c > b) and (b+c > a):
        return True
    return False

for a in range(150):
    for x in range(1000):
        if (trian(x,10,20)) <= (not (max(x, 8) > 24)) == (not trian(3, a, x)):
            pass
        else:
            break
    else:
        ans.append(a)

number = '9'

ans = str(max(ans))
print('Answer: {}'.format(ans))
f = open('homework/301124/ans/'+number+'A.txt','w')
f.write("Answer: "+ans)