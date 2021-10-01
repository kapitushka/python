count = int(input("Введите количество элементов списка: "))
list = []
line = 0
while line < count:
    line_input = input("Введите строку №" + str(line+1) + ": ")
    list.append(line_input)
    line = line + 1

print("Ответ на задание 1.")
print(''.join(list))

print("Ответ на задание 2.")
for line in list:
    print(line[len(line)-1], end=' ')

print()
print("Ответ на задание 3.")
for line in list:
    print(line, len(line))

print("Ответ на задание 4.")
for line in list:
    chars = []
    for char in line:
        chars.append(ord(char))
    print(chr(max(chars)), end=" ")

print()
print("Ответ на задание 5.")
for line in list:
    print(line.upper())

print("Ответ на задание 6.")
for line in sorted(list):
    print(line, end=" ")
