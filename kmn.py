import random

print("----------------------------------------")
print("--- Камень, ножницы, бумага, колодец ---")
print("----------------------------------------")
print(" Правила игры:")
print("Игра состоит из 5-и раундов")
print("Побеждает тот, кто наберет больше очков.")
print("\t[r] - камень\n\t[s] - ножницы\n\t[p] - бумага\n\t[w] - колодец")
player_score = 0
player_select = 0
comp_score = 0
comp_select = 0

print("----------------------------------------")
print("----------- НАЧАЛО ИГРЫ ----------------")
for i in range(5):
    print("--------- РАУНД №" + str(i + 1) + "---------")
    comp_select = random.choice("rpsw")

    while True:
        player_select = input("\tТвой выбор?:")
        if (player_select == "r") or (player_select == "s") or (player_select == "p") or (player_select == "w"):
            break
        else:
            print("\tОшибка! Введите правильную букву:")
    print("\tКомпютер: " + comp_select)

    if player_select == comp_select:
        print("\tНичья!")
    elif player_select == "r" and comp_select == "s":
        player_score = player_score + 1
        print("\tТвоя победа")
    elif player_select == "r" and comp_select == "p":
        comp_score = comp_score + 1
        print("\tВыиграл компьютер!")
    elif player_select == "w" and comp_select == "p":
        comp_score = comp_score + 1
        print("\tВыиграл компьютер!")
    elif player_select == "p" and comp_select == "r":
        player_score = player_score + 1
        print("\tТвоя победа!")
    elif player_select == "w" and comp_select == "s":
        player_score = player_score + 1
        print("\tТвоя победа!")
    elif player_select == "w" and comp_select == "r":
        player_score = player_score + 1
        print("\tТвоя победа!")
    elif player_select == "p" and comp_select == "s":
        comp_score = comp_score + 1
        print("Победил компьютер!")
    elif player_select == "s" and comp_select == "p":
        player_score = player_score + 1
        print("\tТвоя победа!")
    elif player_select == "s" and comp_select == "r":
        comp_score = comp_score + 1
        print("\tПобедил компьютер!")
    elif player_select == "p" and comp_select == "w":
        comp_score = comp_score + 1
        print("Победил компьютер!")
    elif player_select == "s" and comp_select == "w":
        comp_score = comp_score + 1
        print("Победил компьютер!")

print("-------------------------------------")
print("---------- РЕЗУЛЬТАТ ИГРЫ -----------")
if player_score > comp_score:
    print("ПОЗДРАВЛЯЮ! Ты выиграл!")
elif comp_score > player_score:
    print("Извини, компьютер победил!")
else:
    print("НИЧЬЯ!")
