# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12
import re

# ф-ция просто объединяет в единую строку список данных строк, выкидывая пробелы и запятые
def letters_string_to_key(strArray):
    rez = ''
    for el in strArray:
        rez += re.sub('[\,\s]+', '', el.lower())
    return rez

# сделал отдельно строки для русских и английских символов в зависимости от их ценности в игре
letters_en_1_point = 'A, E, I, O, U, L, N, S, T, R'
letters_en_2_points = 'D, G'
letters_en_3_points = 'B, C, M, P'
letters_en_4_points = 'F, H, V, W, Y'
letters_en_5_points = 'K'
letters_en_8_points = 'J, X'
letters_en_10_points = 'Q, Z'
letters_ru_1_point = 'А, В, Е, И, Н, О, Р, С, Т'
letters_ru_2_points = 'Д, К, Л, М, П, У'
letters_ru_3_points = 'Б, Г, Ё, Ь, Я'
letters_ru_4_points = 'Й, Ы'
letters_ru_5_points = 'Ж, З, Х, Ц, Ч'
letters_ru_8_points = 'Ш, Э, Ю'
letters_ru_10_points = 'Ф, Щ, Ъ'

points = [
    (letters_string_to_key([letters_en_1_point, letters_ru_1_point]), 1),
    (letters_string_to_key([letters_en_2_points, letters_ru_2_points]), 2),
    (letters_string_to_key([letters_en_3_points, letters_ru_3_points]), 3),
    (letters_string_to_key([letters_en_4_points, letters_ru_4_points]), 4),
    (letters_string_to_key([letters_en_5_points, letters_ru_5_points]), 5),
    (letters_string_to_key([letters_en_8_points, letters_ru_8_points]), 8),
    (letters_string_to_key([letters_en_10_points, letters_ru_10_points]), 10),
    ]

points_dict = {}

for el in points:
    for letter in el[0]:
        points_dict.update({letter: el[1]})

word = input('Введите слово: ').lower()
if re.match("^\s*[a-z]+\s*$", word) or re.match("^\s*[а-яё]+\s*$", word):

    points = 0
    for letter in word:
        points += points_dict[letter]

    print(f'Слово {word} стоит {points} балл(ов)')

else:
    print('Определитесь с языком ;-)')
