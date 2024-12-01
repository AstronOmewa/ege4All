ans = '\n'

from fnmatch import fnmatch

for i in range(1027110-1027110%4891, 10**10, 4891):
    s = str(i)

    if fnmatch(s,'1?2711*0'):
        ans += f'{s}\n'

print('Answer: {}'.format(ans))


