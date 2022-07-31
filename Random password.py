from random import *

digits = list('0123456789')
lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
punctuation = list('!#$%&*+-=?@^_')
ambiguous_simbols = list('il1Lo0O')
chars = []


def is_valid(num):
    for i in range(len(num)):
        if num[i].isdigit() != True or len(num) == 0:
            return False
            break
    else:
        return True


def get_num(question):
    print(question)
    while True:
        num = input()
        if is_valid(num) and int(num) > 0:
            return int(num)
            break
        else:
            print('Введите целое число больше 0')


def is_has_argument(argument):
    print(f'Должен ли пароль содержать {argument.lower()}? (да/нет)')
    while True:
        answer = input()
        if answer.lower() == 'да':
            return True
            break
        elif answer.lower() == 'нет':
            return False
            break
        else:
            print('Введите "да" или "нет"')


def generate_password(len, chars):
    password = ''
    for i in range(len):
        password += choice(chars)
    return password


def get_chars():
    global chars
    if is_has_argument('Цифры'):
        chars += digits
    if is_has_argument('прописные буквы'):
        chars += uppercase_letters
    if is_has_argument('строчные буквы'):
        chars += lowercase_letters
    if is_has_argument('символы'):
        chars += punctuation
    if is_has_argument('неоднозначные символы'):
        chars += [s for s in ambiguous_simbols if s not in chars]
    else:
        chars = [c for c in chars if c not in ambiguous_simbols]
    return chars


get_chars()
while True:
    if len(chars) > 0:
        pas_length = get_num('Какой длины должен быть пароль?')
        for i in range(get_num('Сколько паролей сгенерировать?')):
            print(generate_password(pas_length, chars))
        break
    else:
        print()
        print('Выберите хотя бы один тип символов, не будьте букой')
        print('Давайте попробуем еще раз')
        print()
        break