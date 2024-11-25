def game(l,r,m):
    if l==r: return (m)%2==0
    if m<0: return 0
    l, r = min(l,r), max(l, r)

    moves = [game(l+1,r,m-1),game(l+2,r,m-1)]

    if (m-1)%2==0: return any(moves)
    else: return all(moves)

print("#19:", max([s for s in range(1,30+1) if not game(15,s,1) and game(15,s,2)]))
print("#20:", sorted([s for s in range(30+1) if not game(15,s,1) and game(15,s,3)][:2]))
print("#21:", [s for s in range(1,30+1) if game(15,s,4) and not game(15,s,2)])

with open('progress_check\\25-11-24\\answers\\19_7-9A.txt','w') as f:
    f.write('19: {}\n 20: {}\n 21: {}'.format(
        max([s for s in range(1,30+1) if not game(15,s,1) and game(15,s,2)]),
        sorted([s for s in range(30+1) if not game(15,s,1) and game(15,s,3)][:2]),
        [s for s in range(1,30+1) if game(15,s,4) and not game(15,s,2)]))