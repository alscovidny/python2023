N = int(input("введите целое число N: "))
# строчка для тестирования пула3
two_n_list = []
a = 1
while 2 ** a <= N:
    two_n_list.append(2**a)
    a+=1
print(*two_n_list, sep=',')
