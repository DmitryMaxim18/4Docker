# with open('cesar', 'r') as file:
#     text = file.read()
#
# alpha_en = [
#     'a', 'b', 'c', 'd', 'e',
#     'f', 'g', 'h', 'i', 'j',
#     'k', 'l', 'm', 'n', 'o',
#     'p', 'q', 'r', 's', 't',
#     'u', 'v', 'w', 'x', 'y',
#     'z'
# ]
#
# alpha_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
#             'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
#             'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
#             'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#
# digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# key = input('input int key')
# new_text = ''
#
# try:
#     for a, i in enumerate(text.lower()):
#         b = text[a]
#         if i.isalpha() and i not in alpha_ru:
#             position = alpha_en.index(i)
#             new_position = (position + int(key)) % len(alpha_en)
#             new_text += alpha_en[new_position] if i == b else alpha_en[new_position].upper()
#         elif i in digits:
#             position = digits.index(i)
#             new_position = (position + int(key)) % len(digits)
#             new_text += digits[new_position]
#         elif i in alpha_ru:
#             position = alpha_ru.index(i)
#             new_position = (position + int(key)) % len(alpha_ru)
#             new_text += alpha_ru[new_position] if i == b else alpha_ru[new_position].upper()
#         else:
#             new_text += i
#     with open('coded_text', 'w') as new_file:
#         new_file.write(new_text)
#     print('*** see changes in coded_text.txt ***')
# except ValueError:
#     print(f'wrong data key: {key} should be integer')
#
#
#
