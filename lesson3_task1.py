# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
#
# Найдите количество и выведите его.

from random import randint

list_1 = [randint(1,9) for _ in range(10)]
k = 3
print(list_1)
print(list_1.count(k))