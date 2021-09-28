"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например: thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"],
    "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""

names = {
    'А': ['Андрей', 'Алексей', 'Александр', 'Алла'],
    'И': ['Иван', 'Илья', 'Игорь'],
    'М': ['Мария', 'Михаил'],
    'П': ['Петр', 'Павел'],
    'С': ['Сергей']
}


def thesaurus(a):
    for key, val in names.items():
        if a[0] == key:
            for item in val:
                if item == a:
                    val.sort()
                    return f'{key}={val}'
    return f'Нет сотрудников с именем {a}'


while True:
    name = input('Введите "Имя" сотрудника: ').title()
    print(thesaurus(name), '\n')
