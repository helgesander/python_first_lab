groupmates = [
    {
        "name": "Никита",
        "surname": "Минеев",
        "exams": ["Электротехника", "Технологии и методы программирования",
                  "Теория вероятности и математическая статистика"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Данил",
        "surname": "Сарачев",
        "exams": ["Электротехника", "Технологии и методы программирования",
                  "Теория вероятности и математическая статистика"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Ульяна",
        "surname": "Филиппова",
        "exams": ["Электротехника", "Технологии и методы программирования",
                  "Теория вероятности и математическая статистика"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Скороходов",
        "exams": ["Электротехника", "Технологии и методы программирования",
                  "Теория вероятности и математическая статистика"],
        "marks": [3, 5, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Вахтин",
        "exams": ["Электротехника", "Технологии и методы программирования",
                  "Теория вероятности и математическая статистика"],
        "marks": [3, 3, 3]
    },
]


def filtration(middle, students):
    lst = []
    for student in students:
        if sum(student["marks"]) / 3 > middle:
            lst.append(student)
    return lst


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(60), u"Экзамены".ljust(66), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(15),
              str(student["exams"])[1:len(str(student["exams"])) - 1].ljust(110),
              str(student["marks"])[1:len(str(student["exams"])) - 1].ljust(20))


middle_number = float(input("Введите среднее значение, по которому будет проходить оценка: "))
list_of_students = filtration(middle_number, groupmates)
print_students(list_of_students)
