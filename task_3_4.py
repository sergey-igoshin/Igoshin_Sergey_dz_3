"""
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
Как поступить, если потребуется сортировка по ключам?
"""

names = {
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"],
        "С": ["Сергей Игошин"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    },
    "П": {
        "А": ["Алексей Петров"]
    }
}


def thesaurus_adv(a, b):
    for key, val in names.items():
        if str(val).find(f"'{a} {b}'") != -1:
            if b[0] == key:
                for _key, _val in val.items():
                    if a[0] == _key:
                        return f'{_key}={_val}'
    return f'Нет сотрудников с именем {a} {b}'


while True:
    name = (input('Введите «Имя Фамилия»: ').title()).split()
    if len(name) == 2:
        print(thesaurus_adv(name[0], name[1]), '\n')
    else:
        print('Неправильный формат ввода\n')
