new_list = []
students = ['Вероника', 'Полина','Алексей', 'Роман', 'Павел', 'Михаил', 'Екатерина']
print("Список студентов:", students)
#print("Студент первый:", students[0])
#print("Студент второйй:", students[1])
#print("Длина имени третьего студента", len(students[1]))
#print("Длина списка:", len(students))
students[0] = "Ника"
print("Студент первый:", students)
isPresent = "Роман"
count = students.count(isPresent)
print(f"Имя {isPresent} встречается {count} раз")
students.append('Валерий')
students.append('Каролина')
students.append('Владимир')
print("Список студентов:", students)
students.insert(0,'Юлия')
print("Список студентов:", students)
students.sort()
print("Список студентов:", students)
students.pop(1)
print("Список студентов:", students)
students.remove('Миша')
print("Список студентов:", students)
