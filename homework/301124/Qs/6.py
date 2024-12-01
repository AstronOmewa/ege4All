from ipaddress import ip_network

n = ip_network('172.16.168.0/255.255.248.0')
ans = 0
for ip in n:
    if f'{ip:b}'.count('1')%5 != 0:
        ans += 1

number = '6'

ans = str(ans)
print('Answer: {}'.format(ans))
f = open('homework/301124/ans/'+number+'A.txt','w')
f.write("Answer: "+ans)