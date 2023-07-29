n = int(input("введите количество монет: ")) #ввод количества монет с клавиатуры
cash = []

for _ in range(n):
    cash.append(int(input("Положение монеты 0: 0 или 1?"))) #ввод положения монеты

if n==1:
    print("не надо переворачивать")
elif n==2:
    if cash.count(1) == cash.count(0):
        print("Кол-во монет, чтобы перевернуть: 1")
    else:
        print("не надо переворачивать")
else:
    print(f'Кол-во монет, чтобы перевернуть: {min(cash.count(1), cash.count(0))}')