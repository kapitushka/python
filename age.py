age = int(input("Сколько вам лет:"))

if (age <= 7):
    print("Ребенок")
elif (age > 7) and (age <= 18):
    print("Вы школьник")
elif(age > 18) and (age <= 23):
    print("Вы студент")
elif(age > 23) and (age <= 60):
    print("Вы работаете")
else:
    print("Вы пенсионер")
