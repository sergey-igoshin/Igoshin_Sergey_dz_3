"""
DZ 2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""

dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(a):
    text = dictionary.get(a.lower(), 'Неправильный запрос')
    if a.islower():
        return text
    else:
        return text.capitalize()


print('"Переводчик c английского на русский язык"')
while True:
    word = input('Введите число от 1 до 10 на английском: ')
    result = num_translate_adv(word)
    print(result)
