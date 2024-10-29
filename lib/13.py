from ipaddress import *

# ip = '192.168.104.109'
# mask  = '255.255.255.252'

# net = [f'{x:b}' for x in ip_network(f'{ip}/{mask}', 0)]
# print(net, sep = '\n')
"""
 В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети 
 относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной 
 конъюнкции к заданному адресу узла и маске сети. Узлы с IP-адресами 176.213.225.119 и 176.213.195.58 находятся в одной сети. 
 Укажите наибольшее возможное значение третьего слева байта маски этой сети. Ответ запишите в виде десятичного числа.
"""

ip1 = '176.213.225.119'
ip2 = '176.213.195.58'

for i in range(16,31):
    m = '1'*i+'0'*(32-i)
    net = [str(x) for x in ip_network(f'{ip1}/{i}', 0)]

    if ip2 in net and ip1 in net[1:-1] and ip2 in net[1:-1]:
        print(IPv4Address(int(m,2)))