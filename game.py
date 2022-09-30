#Игра - угадай число
import random

print("-----Игра - угадай число -----")
print("Привет! Я загадываю число от 1 до 10, а ты должен его угадать")

magic_number = random.randint(1, 10)
user_number = 0
count = 0

while user_number != magic_number:
    user_number = int(input("Введите число:"))
    count = count + 1
    if magic_number > user_number:
        print("Больше!")
    elif magic_number < user_number:
        print("Меньше!")

print("Молодец! Ты угадал!")
print("Я загадал число:" + str(magic_number) +", а ты угадал с " + str(count) + " попытки ")
