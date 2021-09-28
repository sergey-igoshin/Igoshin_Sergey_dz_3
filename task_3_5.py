"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое
слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """функция с удалением используемых элементов"""
    my_list = []
    for item in range(n):
        message = []
        for t in nouns, adverbs, adjectives:
            text = random.choice(t)
            message.append(text)
            t.remove(text)
        my_list.append(' '.join(message))
    return my_list


def get_jokes_adv(n, repeats=True):
    """функция с флагом запрещающим повторы"""
    my_list = []
    for item in range(n):
        message = []
        for t in nouns, adverbs, adjectives:
            text = random.choice(t)
            while text:
                if not repeats:
                    message.append(text)
                    break
                else:
                    text = random.choice(t)

        my_list.append(' '.join(message))
    return my_list


num = int(input(f'Введите число от 1 до {len(min(nouns, adverbs, adjectives))}: '))
print(get_jokes_adv(num, False))
print(get_jokes(num))
