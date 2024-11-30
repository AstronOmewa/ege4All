ans = 0

number = '5'

ans = str(ans)
print('Answer: {}'.format(ans))
f = open('homework/301124/ans/'+number+'A.txt','w')
f.write("Answer: "+ans)