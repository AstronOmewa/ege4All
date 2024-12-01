ans = [10e9]

def isprime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i+=1
    return True

for i in range(0,150):
    for j in range(0,150):
        s = '0' + '1'*i + '2'*j 
        ls = sum(int(x) for x in s)
        if len(s) <= 44: continue

        while any(f in s for f in ['02','01']):
            if '02' in s: s = s.replace('02','1110',1)
            if '01' in s: s = s.replace('01','220',1)
        
        if isprime(sum(int(x) for x in s)):
            ans.append(ls)
            
ans = min(ans)

print('Answer: {}'.format(ans))
