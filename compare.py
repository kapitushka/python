a = int(input("Введите A:"))
b = int(input("Введите B:"))
c = int(input("Введите C:"))

if (a > b) and (a > c):
    print("A больше B и больше C")
elif (a < b) and (a < c):
    print("A меньше B и меньше C")
elif (a > b) and (a < c):
    print("A больше B и меньше C ")
elif (a < b) and (a > c):
    print("A меньше B и больше C")
elif (a == b) and (a > c):
    print("A равно B и больше C")
elif (a == c) and (a < b):
    print("A равно C и меньше B")
elif (a == b) and (a == c):
    print("A, B И C равны")
