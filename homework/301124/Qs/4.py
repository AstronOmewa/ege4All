ans = 0

for n in range(2,10000):
    s = '5' + '2' * n

    while any(f in s for f in ['52','2222','1122']):
        if '52' in s:
            s = s.replace('52','1',1)
        if '2222' in s:
            s = s.replace('2222','5',1)
        if '1122' in s:
            s = s.replace('1122','25')
    res = s
    if sum(int(x) for x in res) == 88:
        ans = n
        break

print('Answer: {}'.format(ans))
