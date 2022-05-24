# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print('Задание 1')
print('')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = dict()

for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

for name in names:
    print(f'{name}: {names[name]}')
print('')

        
# ???


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
print('Задание 2')
print('')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Оля'},
    {'first_name': 'Петя'},
    {'first_name': 'Оля'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = dict()

for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

list_count = list()

for name in names:
    list_count.append(names[name])
list_count = sorted(list_count)
big_number = list_count[-1]

for name in names:
    if names[name] == big_number:
        big_name = name
    else:
        pass

print(f'Самое частое имя среди учеников: {big_name}, кол-во повторений: {big_number}')

print('')

# ???


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print('Задание 3')

print('')

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
        {'first_name': 'Женя'}
    ],
]

classes_list=[]
for school_classes in school_students:
    school_names = dict()
    for student in school_classes:
        if student['first_name'] not in school_names.keys():
            school_names[student['first_name']] = 1
        else:
            school_names[student['first_name']] += 1
    classes_list.append(school_names)

#[
# {'Вася': 2}, 
# {'Маша': 2, 'Оля': 1}, 
# {'Женя': 2, 'Петя': 1, 'Саша': 1}
# ]

for classes_numbers in classes_list:
    list_count = list()
    for name in classes_numbers:
        list_count.append(classes_numbers[name])
    list_count = sorted(list_count)
    big_number = list_count[-1]

    for name in classes_numbers:
        if classes_numbers[name] == big_number:
            big_name = name
    else:
        pass
    print(f'В классе № {(classes_list.index(classes_numbers)+1)} самое частое имя: "{big_name}", число повторений: {big_number}')

print('')

# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

print('Задание 4')

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for school1 in school:
    class1 = school1['students']
    g_number = 0
    b_number = 0
    for name in class1:
        if is_male[name['first_name']] == False:
            g_number += 1
        elif is_male[name['first_name']] == True:
            b_number +=1
        else:
            pass
    print(f'В классе {school1["class"]} девочек: {g_number}, мальчиков: {b_number}')

print('')




# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print('Задание 5')
print('')

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '5a', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
list_classes = list()
for school1 in school:
   
    class1 = school1['students']
    g_number = 0
    b_number = 0
    
    for name in class1:
    
        if is_male[name['first_name']] == False:
            g_number += 1
        elif is_male[name['first_name']] == True:
            b_number +=1
        else:
            pass
    
    classes = {'class': school1['class'], 'девочек' : g_number, 'мальчиков' : b_number}
    list_classes.append(classes)

#[{'class': '2a', 'девочек': 2, 'мальчиков': 0}
#{'class': '3c', 'девочек': 0, 'мальчиков': 2}]
    
list_g_n = list()
for classes1 in list_classes:
    list_g_n.append(classes1['девочек'])
list_g_n = sorted(list_g_n)
g_n = list_g_n[-1]

for classe_g in list_classes:
    if classe_g['девочек'] == g_n:
        print(f'Больше всего девочек в классе {classe_g["class"]}, их количество: {g_n}')

list_g_b = list()
for classes1 in list_classes:
    list_g_b.append(classes1['мальчиков'])
list_g_b = sorted(list_g_b)
g_b = list_g_b[-1]

for classe_b in list_classes:
    if classe_b['мальчиков'] == g_b:
        print(f'Больше всего мальчиков в классе {classe_b["class"]}, их количество: {g_b}')

# ???

