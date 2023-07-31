# list_1 = [1, 2, 3, 4, 5]
# k = 6

from random import randint

list_1 = [91, 51, 73, 6, 29, 77, 27, 76, 65, 10]
k = 48

residual = max(list_1)
number = 0

for j in list_1:
    if abs(k - j) <= residual:
        residual = abs(k - j)
        number = j

print(number)