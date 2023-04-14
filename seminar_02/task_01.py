# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

print("Ведите количество монеток: ")
n = int(input())
coins = []
for i in range(n):
    coins.append(random.randint(0, 1))
print(coins)
eagle = 1
tails = 0
j = 0
sum_eagle = 0
sum_tails = 0
while j < coins:
    if coins[j] == tails:
        sum_tails += 1
    elif coins[j] == eagle:
        sum_eagle += 1
    j += 1

if sum_tails > sum_eagle:
    print("Минимальное количество, которое нужно перевернуть гербом вверх: ")
    print(sum_eagle)
elif sum_tails < sum_eagle:
    print("Минимальное количество, которое нужно перевернуть решкой вверх: ")
    print(sum_tails)
else:
    print("Минимального количества нет")



