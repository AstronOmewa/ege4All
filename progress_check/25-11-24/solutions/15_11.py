#Аналитика

B = [2,5,10,15,17,20,22,25]
C = [2,4,6,8,10,12,15,16,20,25]
A = set()
for x in range(100):
    if not ((x in B) == ((x in A) and (x in C)))<=((x in C) == ((x in A) and (x in B))):
        A.add(x)

print(sum(A))