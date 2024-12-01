cnt, maxsum = 0, 0

with open("homework\\301124\\Qs\\17_data\\17.txt") as f:
    a = [int(x) for x in f.readlines()]
    
    max123 = max(x for x in a if x%1000 == 123)

    for i in range(len(a)-3):
        if (sum(len(str(a[i+k]))==5 for k in range(3)) >= 2) and (sum(a[i+k]%3==0 for k in range(3)) == 1) and (sum(a[i+k] for k in range(3)) > max123):
            cnt += 1
            maxsum = max(maxsum, sum(a[i+k] for k in range(3)))

print('Answer: {}'.format(ans))
