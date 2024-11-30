'''

'''

def game(s1, s2, m):
    if s1+s2 >= 52: return m%2==0
    if m==0: return 0

    h = [game(*move, m-1) for move in [(s1+1,s2), (s1*2, s2), (s1,s2+1), (s1,2*s2)]]

    if (m-1)%2==0:
        return any(h) #хоть один из нынешних должен быть выигрышным, если предыдущий был оппонент
    else:
        return all(h) #все из нынешних должны быть выигрышными, если предыдущий ход был наш. Заметим, что если предыдущим ходом оппонент проиграл,
                      #то нужно, хоть одна из текущих позиций была выигрышной

ans = str(min([s for s in range(1,51) if game(10, s, 3) and not game(10, s, 1)]))

print("#21: {}".format(ans))
f = open('homework/301124/ans/3A.txt','w')
f.write('Answer: {}'.format(ans))