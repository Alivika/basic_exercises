from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

list = [student['first_name'] for student in students]
for key, value in Counter(list).items():
    print(f'{key}: {value}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

list = [student['first_name'] for student in students]
for key, value in Counter(list).most_common(1):
     print(f'Самое частое имя среди учеников: {key}')



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

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
    ],
]

j = 1
for group in school_students:
    list = [student['first_name'] for student in group]
    for key, value in Counter(list).most_common(1):
        print(f'Самое частое имя в классе {j}: {key}')
    j += 1



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 
     'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 
     'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 
     'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def count_genders(school):
    male, female = 0, 0
    for classes in school:
        class_name = classes['class']
        for student in classes['students']:
            if is_male[student['first_name']]:
                male += 1
            else:
                female += 1

        print(f'Класс {class_name}: девочки {female} мальчики {male}')
        male, female = 0, 0

count_genders(school)




# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

def whos_more(school):
    male, female = 0, 0
    for classes in school:
        class_name = classes['class']
        for student in classes['students']:
            if is_male[student['first_name']]:
                male += 1
            else:
                female += 1
        if male > female:
            print(f'Больше всего мальчиков в классе: {class_name}')
        else:
            print(f'Больше всего девочек в классе: {class_name}')
        
        male, female = 0, 0

whos_more(school)