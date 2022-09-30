import random
stats = []
attributes = 5

print("Навыки:", end='')
for i in range(attributes):
    r = random.randint(40, 70)
    stats.append(r)
    print(stats[i], end = ' ')

print(f"\n\t[1] - Прочность {stats[0]}\
    \n\t[2] - Ловкость{stats[1]}\
    \n\t[3] - Интеллект{stats[2]}\
    \n\t[4] - Мудрость{stats[3]}\
    \n\t[5] - Влияние{stats[4]}")

select = int(input("Выбери параметр:"))
#select = select - 1
select -=1

stats[select] = stats[select] + random.randint(5, 10)

for i in range(len(stats)):
    if i ==select:
        continue
    stats[i] = stats[i] - random.randint(5, 10)

print(f"\n\t - Прочность {stats[0]}\
    \n\t - Ловкость{stats[1]}\
    \n\t - Интеллект{stats[2]}\
    \n\t - Мудрость{stats[3]}\
    \n\t - Влияние{stats[4]}")
