from ...lib.exec import task2

print(task2(
    '''
    _ 0 _
    _ _ 0
    _ 0 _
    _ 0 _
    _ 0 _
    _ 1 _
    _ _ 1
    _ 1 _''', [0,0,0,0,0,1,1,1], 'wxy',lambda w,x,y: (x and (w <= y))==1))