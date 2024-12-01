cnt = 0
maxsum = 0
with open('homework/301124/Qs/17_data/17 (1).txt') as f:
    a = [int(x) for x in f.readlines()]

    max538 = max(x for x in a if x%1000==538)

    for i in range(len(a)-3):

        if ((sum(len(str(a[i+k])) == 5 for k in range(4)) >= 2) and any((a[i+k]>10**5-1) or (a[i+k]<10**4) for k in range(4))) and \
            sum(((a[i+k]%3)==0) for k in range(4)) > sum((a[i+k]%7)==0 for k in range(4)) and (2*max538 > sum(a[i+k] for k in range(4)) > max538):
                cnt += 1
                maxsum = max(maxsum, sum(a[i+k] for k in range(4)))

print('Answer: {}'.format(ans))
