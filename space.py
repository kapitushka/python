import random
import turtle
import time
import datetime
import winsound

print('''
******************************************************
*                                                    *
*     Добро пожаловать в космическое путешествие!    *
*                                                    *
******************************************************
''')
print('Инициализация...')
time.sleep(1)

ship = [
'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@@@@@@$___-$$$$$$$@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@@@@-______-$$$$$$$@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@@$__________-$$$$$@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@___-$$$$-_____--$$@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@$___-------$______-@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@_____-------$____-@@@@@@@@@',
'@@@@@@@@@@@@@@$$$$-_______-$$$$$___-@@@@@@@@@@@',
'@@@@@@@@@@@@$$$$$________________$@@@@@@@@@@@@@',
'@@@@@@@@@@$$$$$-_____-$_______-@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@@@@____$$-_____-@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@@@--_$$-_____-$@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@$--$$-____-$$$$@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@$$_--_-$@@@$$$$$@@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@$-__--$@@@@@$$$@@@@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@$$-$$$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@$$$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',]

for i in range(len(ship)):
    print(ship[i])
    time.sleep(0.1)
print('\nУра! Ракета готова!')
print('\n********************************************')
print('\tКОСМИЧЕСКИЙ КОРАБЛЬ ID: ', end='')
name = []
for i in range(5):
    r = random.randint(0,9)
    name.append(r)
    print(name[i], end='')
print('\n\tДата: ', end='')
print(datetime.date.today())
print('\n********************************************')
print('''
Опции:
    [1] - Звезды
    [2] - Галактика
    [3] - Ракета
    [4] - Оборона
    [0] - Выход
''')

winsound.Beep(300, 1000)

while True:
    print('*********************************************************')
    print('*********************************************************')
    select = int(input('Ваш выбор: '))



    # Звезды
    if select == 1 or select == 2:
        turtle.TurtleScreen._RUNNING = True
        turtle.bgcolor('black')
        turtle.speed(0)
        turtle.pensize(1)

        if select == 1:
            print('Звезды рождаются у вас на глазах')
            color = ['white', 'yellow', 'blue', 'purple', 'red', 'lightblue']
            max_index = len(color) - 1

            for i in range(70):
                # Случайные цвета
                random_index = random.randint(0, max_index)
                new_color = color[random_index]
                turtle.color(new_color)
                turtle.begin_fill()
                for i in range(5):
                    turtle.forward(15)
                    turtle.right(144)
                turtle.penup()
                turtle.end_fill()
                # Новое положение в случайном месте
                w = turtle.window_width() // 2 - 50
                h = turtle.window_height() // 2 - 50
                x = random.randrange(-w, w)
                y = random.randrange(-h, h)
                turtle.goto(x, y)
                turtle.pendown()
            turtle.exitonclick()
        # Создаем галактику
        else:
            print('Галактика включает в себя большое количество звезд')
            turtle.pencolor('lightgreen')
            color = ['white', 'yellow']
            max_index = len(color) - 1

            for i in range(200):
                turtle.pensize(i / 100 + 1)
                turtle.forward(i)
                turtle.left(59)
            turtle.exitonclick()
    # Ракета
    elif select == 3:
        print('Запускаем ракету........')
        missle = [
        '#####################################@@',
        '##################################@$@@@',
        '###############################@$-@@@@#',
        '############################@@_$@@@@@##',
        '##########################@-_@@@@@@@###',
        '#######################@@_-@##@@@@@####',
        '#####################@@_-@@@@@@@@@#####',
        '###################@@_-@@@@@@@@@#######',
        '##################@__@@@@@@@@@@########',
        '################@-_@@@@@@@@@@@#########',
        '##############@$_$@@@@@@@@@@###########',
        '#######@@$$$$@$-@@@@@@@@@@@############',
        '#####@$@@@@@@$@@$@@@@@@@@##############',
        '###@$@@@@@@@@@@@@@@@@@@################',
        '##@@@@@@@@@@@@@@@@@@@@#################',
        '#@@@##@@@@@@@@@@@@@@@@#################',
        '#######@@@@@@@@@@@@@@@#################',
        '######-#@@@@@@@@@@@@@##################',
        '####$$-@-####@@@@@@@###################',
        '##$$---$$#####@@@@#####################',
        '#$$--$$#######@@#######################',
        '$$$$$$#################################',
        '$$$####################################'
        ]
        for i in range(len(missle)):
            print(missle[i])
            time.sleep(0.2)
        print('Ракета успешно запущена!')
    elif select == 4:
        print('В нашу сторону движется враг. На наш корабль хотят напасть ID: ', end='')
        for i in range(5):
            print(name[i], end='')
        print('\nСтарт обороны....')
        time.sleep(1)
        protection = [
        '..................._-$@@@$-@_................',
        '.................-$$$$$@@@@$$_...............',
        '.................$$$$@@@@$$@$$_..............',
        '.................-$$$$@@@$$@$-...............',
        '................._@#$$@##@$$-_...............',
        '................._-$$$$$$$$$_................',
        '................._$$@@@@@@$_.................',
        '.................._-@@@@@_...................',
        '.................._-@@#@@$_..................',
        '................_@$$@@@@@@@$_................',
        '..............._@$$$$@@@@##@@$...............',
        '.............._-@@$$$@@@#@#@@@@_.............',
        '.............._@@__$$@@@@@@_.$@@-............',
        '............._@@$._@$@@#@@@_..$@@_...........',
        '............_$@-._-@$@@@@@@..._@@-...........',
        '..........._$@_.._$@$@@#@@@_..._@$_..........',
        '...........-@@$_._@@@@@@@@$_.._@@@$..........',
        '...........$$.__._@@@#_@#@$...$__@$..........',
        '..........._$_..._@@#@_$$@$._...-$_..........',
        '................._@@#@_$@@@-.................',
        '..................$@#@@-@@@$.................',
        '................._$@#@@$@@@@_................',
        '................._--___@@$$@$_...............'
        ]
        for i in range(len(protection)):
            print(protection[i])
            time.sleep(0.2)
    elif select == 0:
        print("Путешествие окончено!")
        break
    else:
        print('Ошибка! Попробуй ещё раз!')
