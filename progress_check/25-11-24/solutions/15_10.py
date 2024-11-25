ashki =[]

for a in range(0,1000):
    for x in range(1,1000):
        if ((x & 45)!=0)<=(((x & 21)==0) <= ((x & a)!=0)):
            continue
        else:
            break
    else:
        ashki.append(a)
B = [x for x in range(20,47+1)]
xes = []
for x in range(1,1000):
    if (x in ashki) and not (x in B):
        xes.append(x)

print(min(xes),ashki)

with open('progress_check\\25-11-24\\answers\\15_10A.txt','w') as f:
    f.write('ans: {}'.format(min(xes)))

