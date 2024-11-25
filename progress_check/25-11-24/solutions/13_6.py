from ipaddress import ip_network, IPv4Address

ip1 = '134.181.67.112'

for m in range(16,31):
    mask = '1'*m+'0'*(32-m)
    mask10 = IPv4Address(int(mask,2))
    ipn1 = [str(x) for x in ip_network(f'{ip1}/{m}',0)]
    if '134.181.94.117' in ipn1[1:-1]:
        print(255+224)

with open('progress_check\\25-11-24\\answers\\13_6A.txt','w') as f:
    f.write('ans: {}'.format(255+224))