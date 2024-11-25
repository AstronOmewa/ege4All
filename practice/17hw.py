"""
В файле содержится последовательность из 10 000 целых положительных чисел. Каждое число не превышает 10 000. 
Определите и запишите в ответе сначала количество пар элементов последовательности, у которых разность элементов кратна 45 и хотя бы один из элементов кратен 18,
затем максимальную из разностей элементов таких пар.
В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
"""
# cnt = 0
# max_diff = -10000

# pairs = set()

# with open('practice/data_17hw/17.txt') as data:
#     lines = [int(x) for x in data.readlines()]

#     for i in range(len(lines)-1):
#         for j in range(i+1,len(lines)):
#             if abs(lines[i]-lines[j])%45 == 0 and (lines[i]%18==0 or lines[j]%18 == 0):
#                 cnt+=1
#                 max_diff = max(max_diff,abs(lines[i]-lines[j]))

# print(cnt, max_diff)

"""
В файле содержится последовательность целых чисел.

Задание 17

Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно. 
Определите количество пар последовательности, в которых только одно число трехзначное, 
и сумма элементов пары кратна минимальному трехзначному значению последовательности, оканчивающемуся на 5. 
В ответе запишите два числа: сначала количество найденных пар, затем минимальную из сумм элементов таких пар. 
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
"""
# cnt = 0
# minxy = 1e7
# with open('practice/data_17hw/17_1.txt') as f:
#     a = [int(x) for x in f.readlines()]
#     min3 = min([x for x in a if len(str(x))==3 and x%10 == 5])

#     for i in range(len(a)-1):
#         x,y = a[i], a[i+1]
#         # print(x,y)
#         if (len(str(x))==3) != (len(str(y))==3) and (x+y)%min3==0:
#             cnt += 1
#             minxy = min(minxy,x+y)

# print(cnt, minxy)


"""
Файл содержит последовательность целых чисел, по модулю не превышающих 10 000. Назовём парой два идущих подряд элемента последовательности.

Задание 17

Определите количество пар, для которых выполняются следующие условия:

—  запись элементов пары заканчивается одной и той же цифрой;

—  ровно один элемент из пары делится без остатка на 3;

—  сумма квадратов элементов пары не превышает квадрат наименьшего из элементов последовательности, запись которых заканчивается цифрой 3.

 

В ответе запишите два числа: сначала количество найденных пар, затем максимальную величину суммы квадратов элементов этих пар.
"""

def solve():
    with open("practice/data_17hw/17_2.txt", "r") as f:
        sequence = [int(x) for x in f.readlines()]

    count = 0
    max_sum_sq = 0
    
    min_num_ending_3 = float('inf')
    for num in sequence:
      if str(num)[-1] == '3':
        min_num_ending_3 = min(min_num_ending_3, num)

    min_num_ending_3_sq = min_num_ending_3**2

    for i in range(len(sequence) - 1):
        a = sequence[i]
        b = sequence[i+1]

        # Условие 1: запись элементов пары заканчивается одной и той же цифрой
        if str(a)[-1] == str(b)[-1]:
            # Условие 2: ровно один элемент из пары делится без остатка на 3
            if (a % 3 == 0 and b % 3 != 0) or (a % 3 != 0 and b % 3 == 0):
                # Условие 3: сумма квадратов элементов пары не превышает квадрат наименьшего из элементов последовательности, запись которых заканчивается цифрой 3
                sum_sq = a**2 + b**2
                if sum_sq <= min_num_ending_3_sq :
                    count += 1
                    max_sum_sq = max(max_sum_sq, sum_sq)

    print(count, max_sum_sq)

solve()