from ipaddress import ip_network

ip = '172.16.8.0'
mask = '255.255.252.0'

ips = ip_network(f'{ip}/{mask}')
ans = int(len(list(ips))/64)
print(ans)

with open('progress_check\\25-11-24\\answers\\13_5A.txt','w') as f:
    f.write('ans: {}'.format(ans))